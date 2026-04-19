from flask import Blueprint, render_template
from flask_login import login_required
from app.models.models import db, Equipo, Mantenimiento, Categoria, Asignacion
from datetime import datetime, timedelta
from sqlalchemy import func

dashboard_bp = Blueprint('dashboard', __name__)


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
    ).join(Equipo).group_by(Categoria.nombre).all()

    labels_cat = [c[0] for c in categorias_data]
    values_cat = [c[1] for c in categorias_data]

    # Alertas de Mantenimiento del Mes
    mes_actual = datetime.now().month
    ano_actual = datetime.now().year
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
                           values_cat=values_cat)