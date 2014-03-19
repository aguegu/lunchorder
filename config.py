import os
from app import app

CSRF_ENABLED = True
SECRET_KEY = 'you-will-never-guess'

basedir = app.root_path

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')
SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
