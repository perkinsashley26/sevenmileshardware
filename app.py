# Flask imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Module imports
from config import Config


class Server(Flask):
    """Server Class for driving the application."""

    def __init__(self):
        """Initialize the class and inherit from super class."""
        super(Server, self).__init__("Seven Miles Hardware")

        # Configure the server
        self.config.from_object(Config)

        # Instantiate other services to achieve singleton pattern
        self.db = SQLAlchemy(self)
        self.bcrypt = Bcrypt(self)

    def db_create_all(self):
        """Create all database tables specified in models."""
        with self.app_context():
            self.db.create_all()
