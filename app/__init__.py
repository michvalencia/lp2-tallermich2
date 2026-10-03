"""
Application factory de la Tienda Virtual (versión con base de datos).

Respecto al Taller 1, create_app() ahora también:
  - carga la configuración desde config.py
  - inicializa la extensión SQLAlchemy
  - registra los comandos de terminal (flask init-db / flask seed-db)
"""

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    basedir = os.path.abspath(os.path.dirname(__file__))

    instance_path = os.path.join(basedir, '..', 'instance')

    os.makedirs(instance_path, exist_ok=True)

    db_file = os.path.join(instance_path, 'app.db')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL') or f'sqlite:///{db_file}'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)

    from app.routes import main as main_blueprint
    app.register_blueprint(main_blueprint)

    from app.commands import register_commands
    register_commands(app)

    return app

