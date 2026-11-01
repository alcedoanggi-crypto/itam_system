from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required
from sqlalchemy.exc import IntegrityError

from app.models.models import db, User

usuarios_bp = Blueprint('usuarios', __name__)

@usuarios_bp.route('/usuarios', methods=['GET', 'POST'])
@login_required
def listar_usuarios():
    if request.method == 'POST':
        try:
            nuevo_usuario = User(
                username=request.form.get('username'),
                nombre=request.form.get('nombre'),
                email=request.form.get('email')
            )
            nuevo_usuario.set_password(request.form.get('password'))
            db.session.add(nuevo_usuario)
            db.session.commit()
            flash('Usuario creado correctamente', 'success')
        except IntegrityError:
            db.session.rollback()
            flash('El usuario o el email ya existen.', 'danger')
        return redirect(url_for('usuarios.listar_usuarios'))

    usuarios = User.query.all()
    return render_template('usuarios.html', usuarios=usuarios)