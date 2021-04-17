from flask import render_template,session, request,url_for,flash,redirect
from shop import app,db,bcrypt
from .forms import RegistrationForm,LoginForm
from .models import User
from shop.products.models import Addproduct,Product,Category
import os

#@app.route('/')
#def home():
#        return render_template('admin/index.html', title='Admin Page')
#, productss=productss

#@app.route('/admin')
#def admin(): 
#    if 'email' not in session:
#       flash(f'Please login first','danger')
#        return redirect(url_for('login'))
#    pproducts= Addproduct.query.all()
#   return render_template('admin/index.html', title='Admin Page', pproducts=pproducts)

@app.route('/products')
def productsman():
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))
    products =Product.query.order_by(Product.id.desc()).all()
    return render_template('admin/product.html',title="Product Page",products=products)

@app.route('/category')
def category():
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))
    categories =Category.query.order_by(Category.id.desc()).all()
    return render_template('admin/product.html',title="Product Page",categories=categories)

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        hash_password= bcrypt.generate_password_hash(form.password.data)
        user = User(name=form.name.data,username=form.username.data, email=form.email.data,
                   password=hash_password)
        db.session.add(user)
        #User.query.delete()
        db.session.commit()
        flash(f'Welcome {form.name.data} Thanks for registering', 'success')
        return redirect(url_for('login'))
    return render_template('admin/register.html', form=form, title="Registration Page")

@app.route('/login', methods=['GET', 'POST'])
def login():
    form= LoginForm(request.form)
    if request.method=="POST" and form.validate():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            session['email']= form.email.data
            flash(f'Welcome {form.email.data} Succesfully Logged In', 'success')
            return redirect(request.args.get('next') or url_for('admin'))
        else:
            flash('Wrong Password Please Try Again', 'danger')
    return render_template('admin/login.html', form= form, title="Login Page")

