from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS
from .config import config
from simplejson import JSONEncoder
from flask_socketio import SocketIO, emit

db = SQLAlchemy()
cors = CORS()
socket = SocketIO()

def init_app(cnf):
    app = Flask(__name__)
    app.config.from_object(config[cnf])
    db.init_app(app)
    cors.init_app(app)
    app.json_encoder = JSONEncoder
    from app.main.routes import main
    app.register_blueprint(main)
    socket.init_app(app, cors_allowed_origins="*")
    return app