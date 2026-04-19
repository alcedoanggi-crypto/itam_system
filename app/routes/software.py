from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.models import db, Software, Equipo

software_bp = Blueprint('software', __name__)

@software_bp.route('/software', methods=['GET', 'POST'])
@login_required
def listar_software():
    if request.method == 'POST':
        try:
            nuevo_soft = Software(
                nombre_software=request.form.get('nombre_software'),
                version=request.form.get('version'),
                clave_licencia=request.form.get('clave_licencia'),
                fecha_vencimiento=request.form.get('fecha_vencimiento') or None,
                equipo_id=request.form.get('equipo_id') or None
            )
            db.session.add(nuevo_soft)
            db.session.commit()
            flash('Software registrado exitosamente', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error al registrar software: {str(e)}', 'danger')
        return redirect(url_for('software.listar_software'))

    softwares = Software.query.all()
    equipos = Equipo.query.all()  # Para vincular en el modal
    return render_template('software.html', softwares=softwares, equipos=equipos)