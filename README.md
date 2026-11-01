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
| Backend           | Python 3.11 + Flask (Blueprints)              |
| Base de datos     | PostgreSQL (gestionada con Flask-SQLAlchemy)  |
| Frontend          | HTML5 (Jinja2), Bootstrap 5, JavaScript       |
| Visualización     | Chart.js (gráficos del panel de control)      |
| Seguridad         | Flask-Login, hash de contraseñas, CSRF (Flask-WTF), variables de entorno (python-dotenv) |

## 🔐 Seguridad

- Contraseñas cifradas con hash (Werkzeug); las cuentas antiguas en texto
  plano se migran automáticamente al iniciar sesión.
- Protección CSRF en todos los formularios.
- Credenciales y clave secreta fuera del código (archivo `.env`).
- Subida de imágenes validada por extensión, con nombre único y límite de 5 MB.

## 📁 Estructura del Proyecto

```
itam_system/
├── app/
│   ├── models/models.py   # Modelos: User, Equipo, Categoria, Ubicacion, MarcaModelo, Software, Asignacion, Mantenimiento
│   ├── routes/            # Un Blueprint por módulo (auth, dashboard, equipos, asignaciones, ...)
│   ├── static/            # CSS, JS y fotos subidas de equipos
│   └── templates/         # Vistas Jinja2
├── docs/screenshots/      # Capturas del README
├── config.py              # Configuración leída desde variables de entorno
├── crear_admin.py         # Crea o actualiza el usuario administrador
├── tecnologico.sql        # Respaldo de PostgreSQL con datos de ejemplo
├── requirements.txt       # Dependencias del proyecto
├── run.py                 # Punto de entrada de la aplicación
└── .env.example           # Plantilla de variables de entorno
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

Crea la base de datos `tecnologico` en PostgreSQL y copia `.env.example`
como `.env`:

```env
SECRET_KEY=una_clave_larga_y_aleatoria
DATABASE_URL=postgresql://usuario:password@localhost:5432/tecnologico?client_encoding=utf8
FLASK_DEBUG=1
```

### 5. Crear las tablas y el usuario administrador

```bash
python crear_admin.py
```

> Opcional: para cargar los datos de ejemplo, restaura el respaldo con
> `pg_restore -d tecnologico tecnologico.sql`

### 6. Ejecutar la aplicación

```bash
python run.py
```

La aplicación estará disponible en `http://127.0.0.1:5000`

**Credenciales de prueba** (creadas por `crear_admin.py`):
- Usuario: `admin`
- Contraseña: `admin123`

---

## 🧪 Próximas Mejoras

- [ ] Editar / eliminar equipos y registrar devoluciones desde la tabla
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
