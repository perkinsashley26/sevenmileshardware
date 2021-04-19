# Import modules required for routing
from flask.views import View
from flask import render_template, request, redirect, url_for, flash, abort, g

# Model imports
from persistence.models.product_models import ProductModel
from persistence.models.user_models import UserModel

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


class AdminViews(object):
    views = {
        'view_orders': ViewOrders,
        'manage_inventory': InventoryManager,
    }