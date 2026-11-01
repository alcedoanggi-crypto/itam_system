import os
import secrets

from dotenv import load_dotenv

load_dotenv()


class Config:
    # Si no hay SECRET_KEY en el entorno se genera una aleatoria (las sesiones
    # se cierran al reiniciar). En producción define siempre SECRET_KEY.
    SECRET_KEY = os.environ.get("SECRET_KEY") or secrets.token_hex(32)
    # Agrega ?client_encoding=utf8 a la URL para evitar UnicodeDecodeError en PostgreSQL
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    WTF_CSRF_ENABLED = True
    MAX_CONTENT_LENGTH = 5 * 1024 * 1024  # 5 MB por archivo subido
