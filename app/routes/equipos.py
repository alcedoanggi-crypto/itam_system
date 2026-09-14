import os
import uuid
from flask import Blueprint, render_template, request, redirect, url_for, flash, current_app
from flask_login import login_required
from werkzeug.utils import secure_filename
from app.models.models import db, Equipo, Categoria, Ubicacion, MarcaModelo
from datetime import datetime  # Importante para manejar la fecha

equipos_bp = Blueprint('equipos', __name__)

EXTENSIONES_PERMITIDAS = {'png', 'jpg', 'jpeg', 'gif', 'webp'}


def _extension_permitida(nombre_archivo):
    return '.' in nombre_archivo and \
        nombre_archivo.rsplit('.', 1)[1].lower() in EXTENSIONES_PERMITIDAS


def _guardar_imagen_equipo(archivo):
    """Guarda la foto del equipo con un nombre único y devuelve el nombre de archivo."""
    if not archivo or archivo.filename == '':
        return None
    if not _extension_permitida(archivo.filename):
        flash('Formato de imagen no válido. Usa PNG, JPG, GIF o WEBP.', 'warning')
        return None

    extension = secure_filename(archivo.filename).rsplit('.', 1)[1].lower()
    nombre_unico = f"{uuid.uuid4().hex}.{extension}"
    archivo.save(os.path.join(current_app.config['UPLOAD_FOLDER'], nombre_unico))
    return nombre_unico


@equipos_bp.route('/equipos', methods=['GET', 'POST'])
@login_required
def listar_equipos():
    if request.method == 'POST':
        # Captura de datos básicos
        numero_serie = request.form.get('numero_serie')
        tipo = request.form.get('tipo')
        marca_modelo_id = request.form.get('marca_modelo_id')
        categoria_id = request.form.get('categoria_id')
        ubicacion_id = request.form.get('ubicacion_id')
        estado = request.form.get('estado')

        # --- PROCESAMIENTO DE LA FECHA ---
        fecha_str = request.form.get('fecha_compra')
        fecha_objeto = None

        if fecha_str:
            # Convertimos el texto 'YYYY-MM-DD' en un objeto datetime
            fecha_objeto = datetime.strptime(fecha_str, '%Y-%m-%d')
        else:
            # Si la fecha es obligatoria y está vacía, enviamos error
            flash('La fecha de compra es obligatoria', 'warning')
            return redirect(url_for('equipos.listar_equipos'))

        # --- FOTO DEL EQUIPO ---
        nombre_imagen = _guardar_imagen_equipo(request.files.get('imagen'))

        nuevo_equipo = Equipo(
            numero_serie=numero_serie,
            tipo=tipo,
            fecha_compra=fecha_objeto,  # Pasamos el objeto fecha convertido
            marca_modelo_id=marca_modelo_id,
            categoria_id=categoria_id,
            ubicacion_id=ubicacion_id,
            estado=estado,
            imagen=nombre_imagen
        )

        try:
            db.session.add(nuevo_equipo)
            db.session.commit()
            flash('¡Equipo registrado exitosamente!', 'success')
        except Exception as e:
            db.session.rollback()
            flash(f'Error al registrar: {str(e)}', 'danger')

        return redirect(url_for('equipos.listar_equipos'))

    # Lógica GET para mostrar la tabla
    equipos = Equipo.query.all()
    categorias = Categoria.query.all()
    ubicaciones = Ubicacion.query.all()
    marcas = MarcaModelo.query.all()

    return render_template(
        'equipos.html',
        equipos=equipos,
        categorias=categorias,
        ubicaciones=ubicaciones,
        marcas=marcas
    )