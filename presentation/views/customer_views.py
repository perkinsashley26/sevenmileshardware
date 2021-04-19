
# Import modules required for routing
from flask.views import View
from flask import render_template, request, redirect, url_for, flash, session

# Model imports
from persistence.models.product_models import ProductModel
from persistence.models.user_models import UserModel
from persistence.models import db

# Form imports
from persistence.forms.user_forms import LoginForm, RegistrationForm


class Home(View):
    """Class based View/Route for the Landing Page."""
    methods = ['GET']
    endpoint = '/'
    name = 'home'

    def dispatch_request(self):
        return render_template("index.html")

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
        form = RegistrationForm(request.form)
        if request.method == 'POST' and form.validate_on_submit():
            print('here')
            user = UserModel(name=form.name.data,username=form.username.data, email=form.email.data,
                    password=form.password.data)
            db.session.add(user)
            #User.query.delete()
            db.session.commit()
            flash(f'Welcome {form.name.data} Thanks for registering', 'success')
            return redirect(url_for('login'))
        return render_template('admin/register.html', form=form, title="Registration Page")


class Login(View):
    """Class based View/Route for Login."""
    methods = ['GET', 'POST']
    endpoint = '/login'
    name = 'login'

    def dispatch_request(self):
        form = LoginForm()
        if request.method=="POST" and form.validate():
            user = UserModel.query.filter_by(email=form.email.data).first()
            if user:
                session['email']= form.email.data
                flash(f'Welcome {form.email.data} Succesfully Logged In', 'success')
                return redirect(request.args.get('next') or url_for('admin'))
            else:
                flash('Wrong Password Please Try Again', 'danger')
        return render_template('admin/login.html', form= form, title="Login Page")

class CustomerViews(object):
    views = {
        'home': Home,
        'catalogue': Catalogue,
        'login': Login,
        'register':Register
    }