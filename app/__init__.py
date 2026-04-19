from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from .models.models import db, User
from .routes.equipos import equipos_bp
from .routes.categorias import categorias_bp
from .routes.software import software_bp
from .routes.ubicaciones import ubicaciones_bp
from .routes.marcas import marcas_bp
from .routes.asignaciones import asignaciones_bp
from .routes.mantenimientos import mantenimientos_bp
from .routes.usuarios import usuarios_bp

def create_app():
    app = Flask(__name__)

    # Configuración
    app.config['SECRET_KEY'] = 'clave_secreta_muy_segura'
    # IMPORTANTE: Para evitar el UnicodeDecodeError en PostgreSQL/SQLAlchemy,
    # asegúrate de que la URL de la base de datos sea correcta.
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:123456@localhost:5432/tecnologico?client_encoding=utf8'
    app.config['SECRET_KEY'] = 'clave_secreta_muy_segura'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # 1. Inicializar la base de datos
    db.init_app(app)

    # 2. CONFIGURACIÓN DE FLASK-LOGIN (Esto quita el AttributeError)
    login_manager = LoginManager()
    login_manager.login_view = 'auth_bp.login' # Redirige aquí si no hay sesión
    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(user_id):
        # Esta función le dice a Flask-Login cómo encontrar al usuario
        return User.query.get(int(user_id))

    # 3. Registro de Blueprints
    from .routes.auth import auth_bp
    from .routes.dashboard import dashboard_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(dashboard_bp)
    app.register_blueprint(equipos_bp)
    app.register_blueprint(categorias_bp)
    app.register_blueprint(software_bp)
    app.register_blueprint(ubicaciones_bp)
    app.register_blueprint(marcas_bp)
    app.register_blueprint(asignaciones_bp)
    app.register_blueprint(mantenimientos_bp)
    app.register_blueprint(usuarios_bp)

    return app