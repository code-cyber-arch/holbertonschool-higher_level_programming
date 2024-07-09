#!/usr/bin/python3
"""Render HTML pages"""
from flask import Flask, render_template
import json

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

if __name__ == '__main__':
    app.run(debug=True, port=5000)
