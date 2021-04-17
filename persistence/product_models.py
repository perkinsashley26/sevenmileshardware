"""Defines SQLAlchemy models for Product data."""
from . import db


class ProductModel(db.Model):
    """Defines the database object model for a Product."""

    pass


class Order(db.Model):
    """Defines the database object model for an Order."""

    pass


class OrderItem(db.model):
    """Defines the database object model for an Order Item."""

    pass


class CategoryModel(db.Model):
    """Defines the database object model for an Order Item."""

    pass
