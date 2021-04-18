"""Defines SQLAlchemy models for Product data."""
from . import db


class ProductModel(db.Model):
    """Defines the database object model for a Product."""
    id = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(100), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    description = db.Column(db.Text,nullable=False)
    stock= db.Column(db.Integer, nullable=False)
    prod_image = db.Column(db.String(150), nullable=False, default='image.jpg')

    pass

# IGNORE FOR NOW
class Order(db.Model):
    """Defines the database object model for an Order."""
    id = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(100), nullable=False) #name of product
    totalprice = db.Column(db.Numeric(10,2), nullable=False) #total price of all products
    quantity= db.Column(db.Integer, nullable=False) #quantity of product ordered
    orderdate=db.Column(db.DateTime, nullable=False,default=datetime.utcnow) #date order was made
    
    pass

class OrderItem(db.model):
    """Defines the database object model for an Order Item."""
    id = db.Column(db.Integer, primary_key=True)
    productname = db.Column(db.String(100), nullable=False) #name of product
    price = db.Column(db.Numeric(10,2), nullable=False) #price of product
    quantity= db.Column(db.Integer, nullable=False) #quantity of product ordered
    description = db.Column(db.Text,nullable=False) #product description
    pass


class CategoryModel(db.Model):
    """Defines the database object model for an Category."""
    id = db.Column(db.Integer, primary_key=True)
    categoryname = db.Column(db.String(100), nullable=False)
    pass
