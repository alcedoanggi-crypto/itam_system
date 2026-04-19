from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_login import login_user, logout_user
from ..models.models import User, db

auth_bp = Blueprint('auth_bp', __name__)

@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        # La consulta ahora será segura gracias al client_encoding en la URI
        user = User.query.filter_by(username=username).first()

        if user and user.password == password:
            login_user(user)
            # Redirige al Blueprint 'dashboard' y su función 'dashboard'
            return redirect(url_for('dashboard.dashboard'))
        else:
            flash('Usuario o contraseña incorrectos', 'danger')

    return render_template('login.html')

@auth_bp.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('auth_bp.login'))
    return redirect(url_for('auth_bp.login'))