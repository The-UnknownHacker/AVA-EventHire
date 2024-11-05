from flask import Flask, render_template, jsonify
import json

app = Flask(__name__)

# Load products from JSON file
with open('products.json') as f:
    products = json.load(f)

@app.route('/')
def index():
    return render_template('index.html', products=products)

@app.route('/product/<int:product_id>')
def product_detail(product_id):
    product = next((item for item in products if item['id'] == product_id), None)
    return render_template('product_detail.html', product=product) if product else "Product not found", 404

if __name__ == '__main__':
    app.run(debug=True)
