# 💻 Sistema de Administración de Equipos Tecnológicos (ITAM)

Aplicación web para el control de equipos tecnológicos de una organización:
inventario de activos, asignación a empleados y mantenimientos.

Este proyecto demuestra desarrollo backend con **Python y Flask**,
arquitectura **MVC**, y persistencia de datos con **PostgreSQL** — inspirado
en experiencia real administrando infraestructura y activos de TI.

![Python](https://img.shields.io/badge/Python-3.11-blue)
![Flask](https://img.shields.io/badge/Flask-2.x-black)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15-blue)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📸 Vista Previa

**Inicio de sesión**
![Inicio de sesión](docs/screenshots/login.png)

**Panel de control**
![Panel de Control](docs/screenshots/dashboard.png)

**Listado de equipos**
![Listado de equipos](docs/screenshots/equipos.png)

**Demo en vivo:** _(agrega aquí el link si despliegas en Render/Railway)_
**Video demostrativo:** _(agrega aquí el link a tu video de TikTok)_

---

## 🚀 Características Principales

- **Inventario de activos:** laptops, monitores, periféricos y licencias de
  software, con número de serie, fecha de compra y estado.
- **Panel de control:** total de equipos, en reparación y disponibles,
  con gráficos por categoría.
- **Asignación de equipos:** vinculación de activos a empleados con
  historial de asignación/devolución.
- **Mantenimientos:** registro de mantenimientos preventivos y correctivos
  con fecha y estado.
- **Categorías de activos:** organización por tipo (hardware, software,
  periféricos, redes).

## 🛠️ Tecnologías Utilizadas

| Categoría        | Tecnología                                   |
|-------------------|-----------------------------------------------|
| Backend           | Python 3.11 + Flask                           |
| Base de datos     | PostgreSQL (gestionada con Flask-SQLAlchemy)  |
| Frontend          | HTML5 (Jinja2), CSS3, JavaScript              |
| Visualización     | Chart.js (gráficos del panel de control)      |
| Seguridad         | Variables de entorno (python-dotenv)          |

## 📁 Estructura del Proyecto

```
itam_system/
├── app/
│   ├── static/        # CSS, JS y recursos estáticos
│   ├── templates/      # Vistas Jinja2 (equipos, asignaciones, dashboard)
│   ├── models.py       # Estructura de la base de datos (Equipo, Empleado, Mantenimiento)
│   └── routes.py       # Lógica de navegación y asignación de activos
├── config.py            # Configuración segura del servidor
├── requirements.txt      # Dependencias del proyecto
├── run.py                # Punto de entrada de la aplicación
└── .env.example           # Ejemplo de variables de entorno requeridas
```

---

## 🔧 Instalación y Uso Local

### 1. Clonar el repositorio

```bash
git clone https://github.com/alcedoanggi-crypto/itam_system.git
cd itam_system
```

### 2. Crear y activar entorno virtual

```bash
python -m venv venv

# En Linux/Mac
source venv/bin/activate

# En Windows
venv\Scripts\activate
```

### 3. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 4. Configurar variables de entorno

Crea un archivo `.env` en la raíz del proyecto basado en `.env.example`:

```env
FLASK_APP=run.py
FLASK_ENV=development
SECRET_KEY=tu_clave_secreta_aqui
DATABASE_URL=postgresql://usuario:password@localhost:5432/itam_db
```

### 5. Crear la base de datos y aplicar migraciones

```bash
flask db upgrade
```

> Si el proyecto no usa Flask-Migrate todavía, inicializa las tablas con:
> `python -c "from app import db; db.create_all()"`

### 6. (Opcional) Cargar datos de prueba

```bash
python seed.py
```

### 7. Ejecutar la aplicación

```bash
flask run
```

La aplicación estará disponible en `http://127.0.0.1:5000`

**Credenciales de prueba** _(si aplica)_:
- Usuario: `admin@demo.com`
- Contraseña: `demo1234`

---

## 🧪 Próximas Mejoras

- [ ] Escaneo de código QR por activo
- [ ] Alertas automáticas de vencimiento de garantía/licencia
- [ ] Tests automatizados con Pytest
- [ ] Despliegue con Docker

## 👩‍💻 Autora

**Anggie Alcedo** — Ingeniera de Sistemas | Full Stack Developer & QA
Automation
[GitHub](https://github.com/alcedoanggi-crypto) ·
[LinkedIn](#) · alcedoanggi@gmail.com

## 📄 Licencia

Este proyecto está bajo la licencia MIT. Ver el archivo `LICENSE` para más
detalles.
