from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from app.models.models import db, Categoria

categorias_bp = Blueprint('categorias', __name__)


@categorias_bp.route('/categorias', methods=['GET', 'POST'])
@login_required
def listar_categorias():
    if request.method == 'POST':
        try:
            nombre = request.form.get('nombre')
            descripcion = request.form.get('descripcion')

            nueva_cat = Categoria(nombre=nombre, descripcion=descripcion)
            db.session.add(nueva_cat)
            db.session.commit()
            flash('Categoría creada exitosamente', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error al crear categoría: {str(e)}', 'danger')
        return redirect(url_for('categorias.listar_categorias'))

    categorias = Categoria.query.all()
    return render_template('categorias.html', categorias=categorias)