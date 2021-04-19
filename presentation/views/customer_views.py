
# Import modules required for routing
from flask.views import View
from flask import render_template, request, redirect, url_for, flash

# Model imports
from persistence.models.product_models import ProductModel
from persistence.models.user_models import UserModel

# Form imports

class Home(View):
    """Class based View/Route for the Landing Page."""
    methods = ['GET']
    endpoint = '/'
    name = 'home'

    def dispatch_request(self):
        return render_template("pages/index.html")

class Catalogue(View):
    """Class based View/Route for the Catalogue."""
    methods = ['GET']
    endpoint = '/catalogue'
    name = 'catalogue'

    def dispatch_request(self):
        return render_template("pages/catalogue.html")

class Register(View):
    """Class based View/Route for Registration."""
    methods = ['GET', 'POST']
    endpoint = "/register"
    name = 'register'

    def dispatch_request(self):
        return render_template("pages/register.html")

class Login(View):
    """Class based View/Route for Login."""
    methods = ['GET', 'POST']
    endpoint = '/login'
    name = 'login'

    def dispatch_request(self):
        return render_template("pages/login.html")

class CustomerViews(object):
    views = {
        'home': Home,
        'catalogue': Catalogue,
        'login': Login,
        'register':Register
    }