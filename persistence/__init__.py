"""Initializes the persistence layer."""
from app import Server

# Instantiate only one instance of the server to adhere to singleton pattern
flask_server = Server(template_dir="presentation/templates", static_path='presentation/static')

from .models import db 

db.init_app(flask_server)
with flask_server.app_context():
    db.create_all()