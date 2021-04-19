# Flask imports
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt

# Module imports
from config import Config
from presentation.views.customer_views import CustomerViews
from presentation.views.admin_views import AdminViews

class Server(Flask):
    """Server Class for driving the application."""

    def __init__(self, template_dir, static_path):
        """Initialize the class and inherit from super class."""
        super(Server, self).__init__("Seven Miles Hardware", static_folder=static_path, template_folder=template_dir)

        # Configure the server
        self.config.from_object(Config)

        # Instantiate other services to achieve singleton pattern
        self.bcrypt = Bcrypt(self)

    def db_create_all(self):
        """Create all database tables specified in models."""
        with self.app_context():
            self.db.create_all()

    def create_views(self):
        """Creates all routes specified in views."""
        # Extract view objects
        customer_views = CustomerViews().views
        admin_views = AdminViews().views

        # Add customer views/routes
        for view in customer_views:
            view_obj = customer_views.get(view)
            endpoint = view_obj.endpoint
            view_name = view_obj.name
            self.add_url_rule(endpoint, view_func=view_obj.as_view(view_name))
        
        # Add admin views/routes
        for view in admin_views:
            view_obj = admin_views.get(view)
            endpoint = view_obj.endpoint
            view_name = view_obj.name
            self.add_url_rule(endpoint, view_func=view_obj.as_view(view_name))
