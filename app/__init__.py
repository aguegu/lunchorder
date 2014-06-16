from flask import Flask
from flask_bootstrap import Bootstrap
from flask.ext.sqlalchemy import SQLAlchemy
from flask.ext.socketio import SocketIO

app = Flask(__name__)
app.config.from_object('config')
Bootstrap(app)
sock = SocketIO(app)
db = SQLAlchemy(app)

from app import views, models
