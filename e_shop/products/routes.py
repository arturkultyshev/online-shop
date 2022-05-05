from flask import render_template, session, request, redirect, url_for, flash,\
     current_app
from e_shop import app, db, photos, search
from .models import Category, Brand, Addproduct
from .forms import Addproducts
import secrets
import os


def brands():
    brands = Brand.query.join(Addproduct,
                              (Brand.id == Addproduct.brand_id)).all()
    return brands

def categories():
    categories = Category.query.join(Addproduct, (Category.id == Addproduct.
                                                  category_id)).all()
    return categories


@app.route('/')
def home():
    page = request.args.get('page', 1, type=int)
    products = Addproduct.query.filter(Addproduct.stock > 0).\
        order_by(Addproduct.id.desc()).paginate(page=page, per_page=8)
    return render_template('products/index.html', products=products,
                           brands=brands(), categories=categories())

@app.route('/result')
def result():
    searchword = request.args.get('q')
    products = Addproduct.query.msearch(searchword, fields=['name', 'desc'],
                                        limit=6)
    return render_template('products/result.html', 
                           products=products, brands=brands(), 
                           categories=categories())

@app.route('/product/<int:id>')
def single_page(id):
    product = Addproduct.query.get_or_404(id)
    return render_template('products/single_page.html', 
                           product=product, 
                           brands=brands(), 
                           categories=categories())


@app.route('/brand/<int:id>')
def get_brand(id):
    page = request.args.get('page', 1, type=int)
    get_brand = Brand.query.filter_by(id=id).first_or_404()
    brand = Addproduct.query.filter_by(brand=get_brand).paginate(page=page,
                                                                 per_page=8)
    return render_template('products/index.html', 
                           brand=brand, brands=brands(), 
                           categories=categories(), 
                           get_brand=get_brand)


@app.route('/categories/<int:id>')
def get_category(id):
    page = request.args.get('page', 1, type=int)
    get_cat = Category.query.filter_by(id=id).first_or_404()
    get_cat_prod = Addproduct.query.filter_by(category=get_cat).\
        paginate(page=page, per_page=8)
    return render_template('products/index.html', 
                           get_cat_prod=get_cat_prod, 
                           brands=brands(), 
                           categories=categories(), 
                           get_cat=get_cat)


@app.route('/addbrand', methods=['GET', 'POST'])
def addbrand():
    if request.method == "POST":
        getbrand = request.form.get('brand')
        brand = Brand(name=getbrand)
        db.session.add(brand)
        flash(f'The brand {getbrand} was added to your database', 'success')
        db.session.commit()
        return redirect(url_for('addbrand'))
    return render_template('products/addbrand.html', title='Add brand', 
                           brands='brands')


@app.route('/updatebrand/<int:id>', methods=['GET', 'POST'])
def updatebrand(id):
    if 'email' not in session:
        flash('Login first please', 'danger')
        return redirect(url_for('login'))
    updatebrand = Brand.query.get_or_404(id)
    brand = request.form.get('brand')
    if request.method =="POST":
        updatebrand.name = brand
        flash(f'The brand {updatebrand.name} was changed to {brand}',
              'success')
        db.session.commit()
        return redirect(url_for('brands'))
    brand = updatebrand.name
    return render_template('products/addbrand.html', title='Udate brand',
                           brands='brands', updatebrand=updatebrand)


@app.route('/deletebrand/<int:id>', methods=['GET', 'POST'])
def deletebrand(id):
    brand = Brand.query.get_or_404(id)
    if request.method == "POST":
        db.session.delete(brand)
        flash(f"The brand {brand.name} was deleted from your database",
              "success")
        db.session.commit()
        return redirect(url_for('admin'))
    flash(f"The brand {brand.name} can't be  deleted from your database",
          "warning")
    return redirect(url_for('admin'))

@app.route('/addcat',methods=['GET', 'POST'])
def addcat():
    if request.method =="POST":
        getcat = request.form.get('category')
        category = Category(name=getcat)
        db.session.add(category)
        flash(f'The brand {getcat} was added to your database', 'success')
        db.session.commit()
        return redirect(url_for('addcat'))
    return render_template('products/addbrand.html', title='Add category')


@app.route('/updatecat/<int:id>', methods=['GET', 'POST'])
def updatecat(id):
    if 'email' not in session:
        flash('Login first please', 'danger')
        return redirect(url_for('login'))
    updatecat = Category.query.get_or_404(id)
    category = request.form.get('category')  
    if request.method == "POST":
        updatecat.name = category
        flash(f'The category {updatecat.name} was changed to {category}','success')
        db.session.commit()
        return redirect(url_for('categories'))
    category = updatecat.name
    return render_template('products/addbrand.html', title='Update cat',
                           updatecat=updatecat)

