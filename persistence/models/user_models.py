"""Defines SQLAlchemy models for User data."""
from . import db
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash


class UserModel(UserMixin, db.Model):
    """The database table for Users Account"""

    __tablename__ = 'users'

    # Database fields
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), unique=False, nullable=False)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(200), nullable=False)
    photo_url = db.Column(db.String(180), nullable=False)

    # Authorization fields
    is_admin= db.Column(db.Boolean ,default=False)

    # Relationships with other tables
    orders_placed = db.relationship(
        "ProductOrderModel",
        cascade="all, delete, delete-orphan", backref="user")

    # username Functions
    def set_password(self,password):
        """Create hased password."""
        self.password = generate_password_hash(password,method='sha256')
    
    def check_password(self,password):
        """Check hashed password."""
        return check_password_hash(self.password,password)
    
