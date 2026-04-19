# 🖥️ EquipoPRO: IT Asset Management System (ITAM)

**EquipoPRO** es una solución integral de nivel empresarial diseñada para el control, seguimiento y mantenimiento de activos tecnológicos. Esta plataforma permite centralizar la gestión de hardware y software, optimizando el ciclo de vida de los equipos y garantizando la continuidad operativa.

![Dashboard de EquipoPRO]
<img width="1365" height="656" alt="image" src="https://github.com/user-attachments/assets/eb0cdc7f-982a-44be-8140-a6d9d188f2c3" />

## 🚀 Funcionalidades Estrella

* **Dashboard Inteligente:** Visualización en tiempo real del estado de los equipos (Disponibles, En Reparación, Total).
* **Gestión de Inventario IT:** Control detallado por Marcas, Modelos, Software y Ubicaciones.
* **Módulo de Reparaciones:** Seguimiento de mantenimientos preventivos y correctivos para reducir el "downtime".
* **Control de Asignaciones:** Registro histórico de movimientos y responsables de cada activo.
* **Interfaz Responsiva:** Diseño profesional, intuitivo y optimizado para la productividad.

## 🛠️ Stack Tecnológico

* **Backend:** Python 3.x con **Flask** (Framework robusto y escalable).
* **Base de Datos:** PostgreSQL (Diseño relacional optimizado para integridad de datos).
* **Frontend:** HTML5, CSS3 (Custom Styles) y **JavaScript** para gráficas dinámicas.
* **Gestión de Archivos:** Sistema de carga de imágenes (Uploads) para documentación visual de equipos.
* **Seguridad:** Implementación de variables de entorno para protección de credenciales sensibles.

## 📁 Estructura Arquitectónica (MVC)

El proyecto sigue una estructura limpia y modular para facilitar su escalabilidad:

- `app/static`: Recursos estáticos (CSS, JS, Dashboards).
- `app/templates`: Vistas dinámicas procesadas con Jinja2.
- `models.py`: Definición del esquema de base de datos relacional.
- `routes.py`: Controladores y lógica de negocio.
- `config.py`: Gestión de configuraciones y seguridad del servidor.

## ⚙️ Instalación Local

1. **Clonar el repositorio:**
   ```bash
   git clone [https://github.com/alcedoanggi-crypto/itam_system.git](https://github.com/alcedoanggi-crypto/itam_system.git)
