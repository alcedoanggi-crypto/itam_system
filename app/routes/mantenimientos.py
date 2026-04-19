# app/routes/mantenimientos.py
from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from ..models.models import db, Mantenimiento, Equipo  #
from datetime import datetime

mantenimientos_bp = Blueprint('mantenimientos', __name__)


@mantenimientos_bp.route('/mantenimientos', methods=['GET', 'POST'])
@login_required
def listar_mantenimientos():
    if request.method == 'POST':
        try:
            # Capturamos el dato del formulario (el 'name' en tu HTML)
            valor_costo = request.form.get('costo')

            # Creamos la instancia usando el nombre de variable que
            # SQLAlchemy reconoce en tu clase Mantenimiento.
            nuevo_manto = Mantenimiento(
                equipo_id=request.form.get('equipo_id'),
                descripcion_reparacion=request.form.get('descripcion'),
                # Usamos el nombre que definiste en models.py (costo_real)
                # y convertimos a float para que no sea nulo.
                costo_real=float(request.form.get('costo')) if request.form.get('costo') else 0.0,
                fecha_proximo_servicio=request.form.get('proximo_servicio')
            )

            db.session.add(nuevo_manto)
            db.session.commit()
            flash('Mantenimiento registrado con éxito', 'success')
            return redirect(url_for('mantenimientos.listar_mantenimientos'))

        except Exception as e:
            db.session.rollback()
            # Mostramos el error exacto para diagnosticar
            flash(f'Error al registrar: {str(e)}', 'danger')
            return redirect(url_for('mantenimientos.listar_mantenimientos'))

    mantenimientos = Mantenimiento.query.all()
    equipos = Equipo.query.all()
    return render_template('mantenimientos.html', mantenimientos=mantenimientos, equipos=equipos)