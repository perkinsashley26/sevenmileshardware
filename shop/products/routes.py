from flask import redirect, render_template,url_for,flash,request, session, current_app
from .forms import Addproducts
from .models import Product,Category,Addproduct
from shop import db, app, photos
import secrets, os

@app.route('/admin')
def admin():    
    pproducts= Addproduct.query.all()
    return render_template('admin/index.html', title='Admin Page', pproducts=pproducts)

@app.route('/customer')
def customer():
    pproducts= Addproduct.query.all()
    return render_template('admin/customer.html', title='Admin Page', pproducts=pproducts)

#ADD PRODUCT MANUFACTURER
@app.route('/addproduct',methods=['GET','POST'])
def addproduct():
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))
    if request.method=="POST":
        getproduct = request.form.get('product')
        product= Product(name=getproduct)
        db.session.add(product)
        flash(f'The Product{getproduct} was successfully added to the database', 'success')
        db.session.commit()
        return redirect(url_for('addproduct'))
    return render_template('products/addproduct.html', products='products')


#UPDATE PRODUCT MANUFACTURER
@app.route('/updateproductman/<int:id>', methods=['GET','POST'])
def updateproductman(id):
    if 'email' not in session:
        flash(f'Please login first','danger')
    updateproductman=Product.query.get_or_404(id)
    product=request.form.get('product')
    if request.method=="POST":
        updateproductman.name=product
        flash(f'Product manufacturer has been updated','success')
        db.session.commit()
        return redirect(url_for('productsman'))
    return render_template('products/updateproductman.html', title='Update Product Manufacturer Page', updateproductman=updateproductman)

#DELETE PRODUCT MANUFACTURER
@app.route('/deleteproduct/<int:id>', methods=['POST'])
def deleteproduct(id):
    deleteproduct= Product.query.get_or_404(id)
    if request.method=="POST":
        db.session.delete(product)
        db.session.commit()
        flash(f'The product manufacturer {product.name} was deleted from the database', 'success')
        return redirect(url_for('admin'))
    flash(f'The product manufacturer {product.name} cannot be deleted', 'warning')
    return redirect(url_for('admin'))

#ADD CATEGORY
@app.route('/addcategory',methods=['GET','POST'])
def addcategory():
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))

    if request.method=="POST":
        getproduct = request.form.get('category')
        category= Category(name=getproduct)
        db.session.add(category)
        flash(f'The Category {getproduct} was successfully added to the database', 'success')
        db.session.commit()
        return redirect(url_for('addcategory'))
    return render_template('products/addproduct.html')

#UPDATE CATEGORY
@app.route('/updatecategory/<int:id>', methods=['GET','POST'])
def updatecategory(id):
    if 'email' not in session:
        flash(f'Please login first','danger')
    updatecategory=Category.query.get_or_404(id)
    category=request.form.get('category')
    if request.method=="POST":
        updatecategory.name=category
        flash(f'Category has been updated','success')
        db.session.commit()
        return redirect(url_for('category'))
    return render_template('products/updateproductman.html', title='Update Category Manufacturer Page', updatecategory=updatecategory)

#ADD PRODUCT
@app.route('/addprod',methods=['POST','GET'])
def addprod():
    if 'email' not in session:
        flash(f'Please login first','danger')
        return redirect(url_for('login'))

    products=Product.query.all()
    categories=Category.query.all()
    form=Addproducts(request.form)
    if request. method =="POST":
        name = form.name.data
        price= form.price.data
        stock= form.stock.data
        description=form.description.data
        product= request.form.get('product')
        category = request.form.get('category')
        image1=photos.save(request.files.get('image1'), name=secrets.token_hex(10)+".")
        image2=photos.save(request.files.get('image2'), name=secrets.token_hex(10)+".")
        image3=photos.save(request.files.get('image3'), name=secrets.token_hex(10)+".")
        addpro =Addproduct(name=name,price=price,stock=stock,description=description,product_id=product,category_id=category,image1=image1,
        image2=image2,image3=image3)
        db.session.add(addpro)
        flash(f'The product {name} has been successfully added to the database', 'success')
        db.session.commit()
        return redirect(url_for('admin'))

    return render_template('products/addprod.html', title="Add Product Page", form= form , products=products, categories=categories)

#UPDATE PRODUCT
@app.route('/updateproduct/<int:id>', methods=['GET','POST'])
def updateproduct(id):
    products=Product.query.all()
    categories= Category.query.all()
    pproduct= Addproduct.query.get_or_404(id)
    product= request.form.get('product')
    category=request.form.get('category')
    form= Addproducts(request.form)
    if request.method=="POST":
        pproduct.name= form.name.data
        pproduct.price=form.price.data
        pproduct.product_id=product
        pproduct.category_id=category
        pproduct.description=form.description.data
        if request.files.get('image1'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + pproduct.image1))
                pproduct.image1=photos.save(request.files.get('image1'), name=secrets.token_hex(10)+".")
            except:
                pproduct.image1=photos.save(request.files.get('image1'), name=secrets.token_hex(10)+".")

        if request.files.get('image2'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + pproduct.image2))
                pproduct.image2=photos.save(request.files.get('image2'), name=secrets.token_hex(10)+".")
            except:
                pproduct.image2=photos.save(request.files.get('image2'), name=secrets.token_hex(10)+".")
       
        if request.files.get('image3'):
            try:
                os.unlink(os.path.join(current_app.root_path, "static/images/" + pproduct.image3))
                pproduct.image3=photos.save(request.files.get('image3'), name=secrets.token_hex(10)+".")
            except:
                pproduct.image3=photos.save(request.files.get('image3'), name=secrets.token_hex(10)+".")
        
        db.session.commit()
        flash(f'Product has been updated','success')
        return redirect(url_for('admin'))
    form.name.data=pproduct.name
    form.price.data=pproduct.price
    form.stock.data=pproduct.stock
    form.description.data=pproduct.description
    return render_template('products/updateproduct.html', form=form, products=products,categories=categories, pproduct=pproduct)