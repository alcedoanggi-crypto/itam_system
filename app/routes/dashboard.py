from flask import Blueprint, render_template
from flask_login import login_required
from app.models.models import db, Equipo, Mantenimiento, Categoria, Asignacion
from datetime import datetime, timedelta
from sqlalchemy import func, extract

dashboard_bp = Blueprint('dashboard', __name__)

MESES = ['Ene', 'Feb', 'Mar', 'Abr', 'May', 'Jun', 'Jul', 'Ago', 'Sep', 'Oct', 'Nov', 'Dic']


@dashboard_bp.route('/dashboard')
@login_required
def dashboard():
    # KPIs Básicos
    total_equipos = Equipo.query.count()
    equipos_reparacion = Equipo.query.filter_by(estado='En Reparación').count()
    equipos_disponibles = Equipo.query.filter_by(estado='Disponible').count()

    # Datos para Gráfico de Categorías
    categorias_data = db.session.query(
        Categoria.nombre, func.count(Equipo.id)
    ).join(Equipo).group_by(Categoria.nombre).order_by(func.count(Equipo.id).desc()).all()

    labels_cat = [c[0] for c in categorias_data]
    values_cat = [c[1] for c in categorias_data]

    # Datos para Gráfico de Equipos por Estado
    estado_data = db.session.query(
        Equipo.estado, func.count(Equipo.id)
    ).group_by(Equipo.estado).order_by(func.count(Equipo.id).desc()).all()

    labels_estado = [e[0] or 'Sin estado' for e in estado_data]
    values_estado = [e[1] for e in estado_data]

    # Equipos adquiridos por mes (año actual), para la gráfica de actividad
    ano_actual = datetime.now().year
    registros_mes = db.session.query(
        extract('month', Equipo.fecha_compra), func.count(Equipo.id)
    ).filter(
        extract('year', Equipo.fecha_compra) == ano_actual
    ).group_by(extract('month', Equipo.fecha_compra)).all()

    conteo_por_mes = {int(mes): cantidad for mes, cantidad in registros_mes}
    values_actividad = [conteo_por_mes.get(i, 0) for i in range(1, 13)]

    # Alertas de Mantenimiento del Mes
    mes_actual = datetime.now().month
    alertas_mantenimiento = Mantenimiento.query.filter(
        db.extract('month', Mantenimiento.fecha_proximo_servicio) == mes_actual,
        db.extract('year', Mantenimiento.fecha_proximo_servicio) == ano_actual
    ).all()

    return render_template('dashboard.html',
                           total_equipos=total_equipos,
                           equipos_reparacion=equipos_reparacion,
                           equipos_disponibles=equipos_disponibles,
                           alertas_mantenimiento=alertas_mantenimiento,
                           labels_cat=labels_cat,
                           values_cat=values_cat,
                           labels_estado=labels_estado,
                           values_estado=values_estado,
                           labels_actividad=MESES,
                           values_actividad=values_actividad,
                           ano_actual=ano_actual)
