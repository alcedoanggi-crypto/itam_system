from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.models import db, Equipo, Categoria, Ubicacion, MarcaModelo
from datetime import datetime  # Importante para manejar la fecha

equipos_bp = Blueprint('equipos', __name__)


@equipos_bp.route('/equipos', methods=['GET', 'POST'])
@login_required
def listar_equipos():
    if request.method == 'POST':
        # Captura de datos básicos
        numero_serie = request.form.get('numero_serie')
        tipo = request.form.get('tipo')
        marca_modelo_id = request.form.get('marca_modelo_id')
        categoria_id = request.form.get('categoria_id')
        ubicacion_id = request.form.get('ubicacion_id')
        estado = request.form.get('estado')

        # --- PROCESAMIENTO DE LA FECHA ---
        fecha_str = request.form.get('fecha_compra')
        fecha_objeto = None

        if fecha_str:
            # Convertimos el texto 'YYYY-MM-DD' en un objeto datetime
            fecha_objeto = datetime.strptime(fecha_str, '%Y-%m-%d')
        else:
            # Si la fecha es obligatoria y está vacía, enviamos error
            flash('La fecha de compra es obligatoria', 'warning')
            return redirect(url_for('equipos.listar_equipos'))

        nuevo_equipo = Equipo(
            numero_serie=numero_serie,
            tipo=tipo,
            fecha_compra=fecha_objeto,  # Pasamos el objeto fecha convertido
            marca_modelo_id=marca_modelo_id,
            categoria_id=categoria_id,
            ubicacion_id=ubicacion_id,
            estado=estado
        )

        try:
            db.session.add(nuevo_equipo)
            db.session.commit()
            flash('¡Equipo registrado exitosamente!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error al registrar: {str(e)}', 'danger')

        return redirect(url_for('equipos.listar_equipos'))

    # Lógica GET para mostrar la tabla
    equipos = Equipo.query.all()
    categorias = Categoria.query.all()
    ubicaciones = Ubicacion.query.all()
    marcas = MarcaModelo.query.all()

    return render_template(
        'equipos.html',
        equipos=equipos,
        categorias=categorias,
        ubicaciones=ubicaciones,
        marcas=marcas
    )