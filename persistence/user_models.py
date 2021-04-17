"""Defines SQLAlchemy models for User data."""
from . import db


class UserModel(db.Model):
    """The database table for Users."""

    __tablename__ = 'users'

    # Database fields
    id = db.Column(db.Integer, primary_key=True)
    first_name = db.Column(db.String(100), nullable=False)
    last_name = db.column(db.String(100), nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    photo_url = db.Column(db.String(180), nullable=False)

    # Authorization fields

    # Relationships with other tables
    orders_placed = db.relationship(
        "ProductOrderModel",
        cascade="all, delete, delete-orphan", backref="user")
