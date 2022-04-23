from flask import Flask, render_template


app = Flask(__name__)


@app.route('/menu')
def explain():
    return render_template('index.html')


@app.route('/products')
def all_products():
    return render_template('products.html')


@app.route('/detail')
def login():
    return render_template('product-detail.html')


@app.route('/reg')
def registrate():
    return render_template('log.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
