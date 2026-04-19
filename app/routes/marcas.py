from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.models import db, MarcaModelo

marcas_bp = Blueprint('marcas', __name__)

@marcas_bp.route('/marcas', methods=['GET', 'POST'])
@login_required
def listar_marcas():
    if request.method == 'POST':
        try:
            nueva_marca = MarcaModelo(
                nombre_marca=request.form.get('nombre_marca'),
                modelo=request.form.get('modelo'),
                fabricante=request.form.get('fabricante')
            )
            db.session.add(nueva_marca)
            db.session.commit()
            flash('Marca y Modelo registrados con éxito', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error al registrar: {str(e)}', 'danger')
        return redirect(url_for('marcas.listar_marcas'))

    marcas = MarcaModelo.query.all()
    return render_template('marcas.html', marcas=marcas)