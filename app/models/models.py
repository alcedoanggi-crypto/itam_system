from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin

db = SQLAlchemy()

# 1. USUARIOS
class User(UserMixin, db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    nombre = db.Column(db.String(100))
    email = db.Column(db.String(100), unique=True)
    asignaciones = db.relationship('Asignacion', backref='usuario', lazy=True)

# 2. CATEGORÍAS
class Categoria(db.Model):
    __tablename__ = 'categorias'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre = db.Column(db.String(50), nullable=False)
    descripcion = db.Column(db.Text)
    equipos = db.relationship('Equipo', backref='categoria', lazy=True)

# 3. UBICACIONES
class Ubicacion(db.Model):
    __tablename__ = 'ubicaciones'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_sala = db.Column(db.String(100), nullable=False)
    piso = db.Column(db.String(20))
    sede = db.Column(db.String(50))
    equipos = db.relationship('Equipo', backref='ubicacion', lazy=True)

# 4. MARCAS Y MODELOS (Corregido a singular para consistencia)
class MarcaModelo(db.Model):
    __tablename__ = 'marcas_modelos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_marca = db.Column(db.String(50), nullable=False)
    modelo = db.Column(db.String(50))
    fabricante = db.Column(db.String(50))
    equipos = db.relationship('Equipo', backref='marca_modelo', lazy=True)

# 5. EQUIPOS
class Equipo(db.Model):
    __tablename__ = 'equipos'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    numero_serie = db.Column(db.String(100), unique=True, nullable=False)
    tipo = db.Column(db.String(50)) 
    fecha_compra = db.Column(db.Date)
    estado = db.Column(db.String(50)) 
    imagen = db.Column(db.String(200))

    categoria_id = db.Column(db.Integer, db.ForeignKey('categorias.id'))
    ubicacion_id = db.Column(db.Integer, db.ForeignKey('ubicaciones.id'))
    marca_modelo_id = db.Column(db.Integer, db.ForeignKey('marcas_modelos.id'))

    mantenimientos = db.relationship('Mantenimiento', backref='equipo', lazy=True)
    asignaciones = db.relationship('Asignacion', backref='equipo', lazy=True)
    software_instalado = db.relationship('Software', backref='equipo', lazy=True)
    historial_estados = db.relationship('HistorialEstado', backref='equipo', lazy=True)

# 6. SOFTWARE
class Software(db.Model):
    __tablename__ = 'software'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    nombre_software = db.Column(db.String(100), nullable=False)
    version = db.Column(db.String(50))
    clave_licencia = db.Column(db.String(100))
    fecha_vencimiento = db.Column(db.Date)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'))

# 7. HISTORIAL DE ESTADOS
class HistorialEstado(db.Model):
    __tablename__ = 'historial_estados'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'), nullable=False)
    estado_anterior = db.Column(db.String(50))
    estado_nuevo = db.Column(db.String(50))
    fecha_cambio = db.Column(db.DateTime, default=datetime.utcnow)
    motivo = db.Column(db.Text)

# 8. ASIGNACIONES
class Asignacion(db.Model):
    __tablename__ = 'asignaciones'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'), nullable=False)
    usuario_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    fecha_entrega = db.Column(db.DateTime, default=datetime.utcnow)
    fecha_devolucion = db.Column(db.DateTime, nullable=True)

# 9. MANTENIMIENTOS
class Mantenimiento(db.Model):
    __tablename__ = 'mantenimientos'
    id = db.Column(db.Integer, primary_key=True)
    equipo_id = db.Column(db.Integer, db.ForeignKey('equipos.id'), nullable=False)
    descripcion_reparacion = db.Column(db.Text)
    costo_real = db.Column('costo', db.Numeric(10, 2), nullable=False)
    fecha_proximo_servicio = db.Column(db.Date)
    fecha_registro = db.Column(db.DateTime, default=datetime.utcnow)