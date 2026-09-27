"""
Application factory de la Tienda Virtual (versión con base de datos).

Respecto al Taller 1, create_app() ahora también:
  - carga la configuración desde config.py
  - inicializa la extensión SQLAlchemy
  - registra los comandos de terminal (flask init-db / flask seed-db)
"""

from flask import Flask
from config import Config
from app.extensions import db

def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)

    # Inicializar SQLAlchemy con la aplicación
    db.init_app(app)

    # Registrar los comandos personalizados de la terminal
    from app.commands import registrar_comandos
    registrar_comandos(app)

    # Importar los modelos dentro del contexto para que Flask-SQLAlchemy los detecte
    with app.app_context():
        from app import models

    return app
