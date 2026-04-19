from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.models import db, Asignacion, Equipo, User
from datetime import datetime
from sqlalchemy import func, cast, String

# Definición del Blueprint para organizar las rutas de asignaciones
asignaciones_bp = Blueprint('asignaciones', __name__)


@asignaciones_bp.route('/asignaciones', methods=['GET', 'POST'])
@login_required
def listar_asignaciones():
    """
    Maneja la visualización de la lista de asignaciones (GET)
    y el registro de nuevas entregas de equipos (POST).
    """
    if request.method == 'POST':
        try:
            # 1. Obtener datos del formulario enviados por el modal
            equipo_id = request.form.get('equipo_id')
            usuario_id = request.form.get('usuario_id')

            # Validación básica para asegurar que se seleccionaron IDs
            if not equipo_id or not usuario_id:
                flash('Por favor, seleccione un equipo y un usuario.', 'warning')
                return redirect(url_for('asignaciones.listar_asignaciones'))

            # 2. Crear el nuevo registro de Asignación
            nueva_asig = Asignacion(
                equipo_id=int(equipo_id),
                usuario_id=int(usuario_id),
                fecha_entrega=datetime.now()  # Registra la hora actual del servidor
            )

            # 3. Actualizar el estado del equipo de forma automática
            # Buscamos el equipo en la base de datos por su ID
            equipo = Equipo.query.get(equipo_id)
            if equipo:
                # Cambiamos su estado para que deje de estar disponible
                equipo.estado = 'Asignado'

            # 4. Guardar los cambios en la base de datos
            db.session.add(nueva_asig)
            db.session.commit()

            flash('Asignación registrada con éxito. El equipo ahora figura como Asignado.', 'success')

        except Exception as e:
            # En caso de error, deshacemos cualquier cambio pendiente
            db.session.rollback()
            flash(f'Error al registrar la asignación: {str(e)}', 'danger')

        return redirect(url_for('asignaciones.listar_asignaciones'))

    # --- Lógica para el método GET (Carga de la página) ---

    # Consultamos todas las asignaciones para la tabla principal
    # Usamos .order_by para ver las más recientes primero
    asignaciones = Asignacion.query.order_by(Asignacion.fecha_entrega.desc()).all()

    # Consultamos equipos disponibles para el dropdown del modal
    # Usamos func.lower para evitar errores si "Disponible" se escribió distinto
    equipos_disponibles = Equipo.query.filter(
        func.lower(cast(Equipo.estado, String)) == 'disponible'
    ).all()

    # Consultamos todos los usuarios para el dropdown de responsables
    usuarios = User.query.all()

    return render_template(
        'asignaciones.html',
        asignaciones=asignaciones,
        equipos=equipos_disponibles,
        usuarios=usuarios
    )