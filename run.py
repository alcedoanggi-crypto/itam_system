from app import create_app
import sys
import os

# Iniciamos la aplicación
app = create_app()

if __name__ == '__main__':
    # El modo debug=True es fundamental para que el servidor no se cierre
    app.run(debug=True)