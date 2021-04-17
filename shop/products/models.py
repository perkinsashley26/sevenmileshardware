from shop import db
from datetime import datetime


class Addproduct(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    description = db.Column(db.Text, nullable=False)
    stock= db.Column(db.Integer, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False,
        default=datetime.utcnow)

    product_id = db.Column(db.Integer, db.ForeignKey('product.id'),nullable=False)
    product = db.relationship('Product',backref=db.backref('products', lazy=True))

    category_id = db.Column(db.Integer, db.ForeignKey('category.id'),nullable=False)
    category = db.relationship('Category',backref=db.backref('posts', lazy=True))

    image1 = db.Column(db.String(150), nullable=False, default='image.jpg')
    image2 = db.Column(db.String(150), nullable=False, default='image.jpg')
    image3 = db.Column(db.String(150), nullable=False, default='image.jpg')

    def __repr__(self):
        return '<Addproduct %r>' % self.title

class Product(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30), nullable=False, unique=True)

class Category(db.Model):
    id= db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(30), nullable=False, unique=True)

db.create_all()