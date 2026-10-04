# Catálogo de Productos - Taller Flask

Aplicación web desarrollada en Python con Flask para la gestión y visualización de un catálogo de productos organizados por categorías.

# Instalación y Configuración
Clonar el repositorio

   ```bash
   git clone [https://github.com/TU_USUARIO/lp2-tallermich2.git](https://github.com/TU_USUARIO/lp2-tallermich2.git)
   cd lp2-tallermich2

1. Crear y activar el entorno virtual:
python3 -m venv venv
source venv/bin/activate

2.Instalar las dependencias
pip install -r requirements.txt

4. Ejecución del proyecto
flask run                - Navegador http://127.0.0.1:5000

5. Estructura del proyecto

lp2-tallermich2/
├── app/
│   ├── data/           # Archivos JSON de datos iniciales
│   ├── static/         # Estilos CSS, imágenes y scripts
│   ├── templates/      # Plantillas HTML (Jinja2)
│   ├── commands.py     # Comandos CLI personalizados de Flask
│   ├── models.py       # Modelos de SQLAlchemy
│   └── routes.py       # Rutas y vistas de la aplicación
├── instance/           # Base de datos SQLite local
├── config.py           # Configuración del entorno Flask
├── run.py              # Punto de entrada de la aplicación
└── requirements.txt    # Dependencias del proyecto




