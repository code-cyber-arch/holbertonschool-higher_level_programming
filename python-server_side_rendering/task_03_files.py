#!/usr/bin/python3
"""Render HTML pages"""
import json
import csv
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    """Render home page"""
    return render_template('index.html')

@app.route('/about')
def about():
    """Render about page"""
    return render_template('about.html')

@app.route('/contact')
def contact():
    """Render contact page"""
    return render_template('contact.html')

@app.route('/items')
def show_items():
    """Render items page"""
    try:
        with open('items.json', 'r') as file:
            items_data = json.load(file)
            items = items_data.get('items', [])
    except FileNotFoundError:
        items = []
    
    return render_template('items.html', items=items)


@app.route('/products')
def display_products():
    source = request.args.get('source')
    id = request.args.get('id')

    if source not in ['json', 'csv']:
        return render_template('product_display.html', error='Wrong source')
    
    try:
        if source == 'json':
            with open('products.json', 'r') as file:
                products = json.load(file)
        elif source == 'csv':
            with open('products.csv', 'r', newline='') as file:
                reader = csv.DictReader(file)
                products = [row for row in reader]
        
        if id:
            data = [product for product in products if str(product.get('id')) == id]
            if not data:
                return render_template('product_display.html', error='Product not found')
            products = data
        return render_template('product_display.html', products=products)
    except Exception as e:
        return render_template('product_display.html', error=str(e))


if __name__ == '__main__':
    app.run(debug=True, port=5000)
