"""Crea (o actualiza) un usuario para iniciar sesion en itam_system.

Uso:
    python crear_admin.py                      -> admin / admin123
    python crear_admin.py juan MiClave123      -> juan  / MiClave123
"""
import sys

from app import create_app
from app.models.models import db, User

usuario = sys.argv[1] if len(sys.argv) > 1 else "admin"
clave = sys.argv[2] if len(sys.argv) > 2 else "admin123"

app = create_app()
with app.app_context():
    db.create_all()  # crea las tablas si aun no existen

    u = User.query.filter_by(username=usuario).first()
    if u:
        accion = "actualizado"
    else:
        u = User(username=usuario, nombre="Administrador", email=f"{usuario}@itam.local")
        db.session.add(u)
        accion = "creado"
    u.set_password(clave)  # se guarda cifrada (hash), nunca en texto plano

    db.session.commit()
    print(f"Usuario '{usuario}' {accion}. Contrasena: {clave}")
    print("Total de usuarios en la BD:", User.query.count())
