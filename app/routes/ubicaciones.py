from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.models import db, Ubicacion

ubicaciones_bp = Blueprint('ubicaciones', __name__)

@ubicaciones_bp.route('/ubicaciones', methods=['GET', 'POST'])
@login_required
def listar_ubicaciones():
    if request.method == 'POST':
        try:
            nueva_ubi = Ubicacion(
                nombre_sala=request.form.get('nombre_sala'),
                piso=request.form.get('piso'),
                sede=request.form.get('sede')
            )
            db.session.add(nueva_ubi)
            db.session.commit()
            flash('Ubicación registrada correctamente', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error al registrar ubicación: {str(e)}', 'danger')
        return redirect(url_for('ubicaciones.listar_ubicaciones'))

    ubicaciones = Ubicacion.query.all()
    return render_template('ubicaciones.html', ubicaciones=ubicaciones)