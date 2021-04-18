"""Defines SQLAlchemy models for Product data."""
from . import db
import datetime


class ProductModel(db.Model):
    """Defines the database object model for a Product."""

    __tablename__ = 'products'

    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    description = db.Column(db.Text,nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    prod_image = db.Column(db.String(150), nullable=False)

    # Relationships with other tables
    category_id = db.Column(
        db.Integer,
        db.ForeignKey("product_categories.id"),
        nullable=False
    )


class OrderModel(db.Model):
    """Defines the database object model for an Order."""

    __tablename__ = 'orders'

    id = db.Column(db.Integer, primary_key=True)

    # Total price of all products in order
    total_price = db.Column(db.Numeric(10,2), nullable=False) 

    # Quantity of product ordered
    quantity = db.Column(db.Integer, nullable=False) 

    # Date order was made
    order_date=db.Column(
        db.DateTime, unique=False, nullable=False,default=datetime.utcnow) 
    
    complete = db.Column(db.Boolean, default=False)

    # Relationships with other tables
    order_items = db.relationship(
        "OrderItemModel", cascade="all, delete", backref="order")

    user_id = db.Column(
        db.Integer, db.ForeignKey('users.id'), nullable=False)

    

class OrderItemModel(db.model):
    """Defines the database object model for an Order Item."""

    __tablename__ = 'order_items'

    id = db.Column(db.Integer, primary_key=True)

    # Price of product
    price = db.Column(db.Numeric(10,2), nullable=False) 

    # Quantity of product
    quantity= db.Column(db.Integer, nullable=False)

    # Relationships with other tables
    order_id = db.Column(
        db.Integer, db.ForeignKey("orders.id"), nullable=False)

    product_id = db.Column(
        db.Integer, db.ForeignKey("products.id"), nullable=False)



class CategoryModel(db.Model):
    """Defines the database object model for an Category."""

    __tablename__ = 'product_categories'

    id = db.Column(db.Integer, primary_key=True)
    category_name = db.Column(db.String(100), nullable=False)

