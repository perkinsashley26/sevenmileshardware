"""Initializes the persistence layer."""
from app import Server

# Instantiate only one instance of the server to adhere to singleton pattern
flask_server = Server()
db = flask_server.db
