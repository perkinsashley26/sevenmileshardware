# Import modules required for routing
from flask.views import View
from flask import render_template, request, redirect, url_for, flash, abort, g, session

# Model imports
from persistence.models.product_models import ProductModel, CategoryModel
from persistence.models.user_models import UserModel
from persistence.models import db

def user_required(f):
    """Checks whether user is logged in or raises error 401."""
    def decorator(*args, **kwargs):
        if not g.user:
            abort(401)
        return f(*args, **kwargs)
    return decorator


class ViewOrders(View):
    """Class based View/Route for the View Orders Page."""
    methods = ['GET', 'POST', 'PUT']
    endpoint = '/admin/view_orders'
    name = 'view_orders'

    def dispatch_request(self):
        return render_template("pages/view_orders.html")

class InventoryManager(View):
    """Class based View/Route for the Product Manager Page."""
    methods = ['GET', 'POST', 'PUT']
    endpoint = '/admin/inventory_manager'
    name = 'inventory_manager'

    def dispatch_request(self):
        return render_template("pages/manage_inventory.html")

class AddProduct(View):
    """Class based View/Route for the Product Manager Page."""
    methods = ['GET', 'POST', 'PUT']
    endpoint = '/admin/add_product'
    name = 'add_product'

    def dispatch_request(self):
        if 'email' not in session:
            flash(f'Please login first','danger')
            return redirect(url_for('login'))
        if request.method=="POST":
            getproduct = request.form.get('product')
            product= ProductModel(name=getproduct)
            db.session.add(product)
            flash(f'The Product{getproduct} was successfully added to the database', 'success')
            db.session.commit()
            return redirect(url_for('addproduct'))
        return render_template('products/addproduct.html', products='products')

class AddCategory(View):
    """Class based View/Route for the Product Manager Page."""
    methods = ['GET', 'POST', 'PUT']
    endpoint = '/admin/add_category'
    name = 'add_category'
    
    def dispatch_request(self):
        if 'email' not in session:
            flash(f'Please login first','danger')
            return redirect(url_for('login'))

        if request.method=="POST":
            getproduct = request.form.get('category')
            category = CategoryModel(name=getproduct)
            db.session.add(category)
            flash(f'The Category {getproduct} was successfully added to the database', 'success')
            db.session.commit()
            return redirect(url_for('addcategory'))
        return render_template('products/addproduct.html')

class AdminViews(object):
    views = {
        'view_orders': ViewOrders,
        'manage_inventory': InventoryManager,
        'add_product': AddProduct,
        'add_category': AddCategory
    }