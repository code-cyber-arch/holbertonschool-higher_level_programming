#!/usr/bin/python3

from flask import Flask, render_template, request
from pathlib import Path
import json
import csv
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/items')
def items():
    items_list = []

    with open("items.json", 'r') as f:
        rows = json.load(f)
    for key,value in rows.items():
        items_list = value

    return render_template('items.html', items=items_list)

@app.route('/products')
def products():
    source = request.args.get('source')
    id = request.args.get('id')

    data = []
    if source == "json":
        data = load_json_data("products.json", id)
    elif source == "csv":
        data = load_csv_data("products.csv", id)
    elif source == "sql":
        sql_filepath = "products.db"
        # create sqlite file if it doesn't exist yet
        if not Path(sql_filepath).is_file():
            create_sql_data(sql_filepath)

        data = load_sql_data(sql_filepath, id)

    return render_template('product_display.html', data=data, source=source, id=id)

def load_json_data(filename, wanted_id = None):
    """ Load JSON data from file and returns as dictionary """

    data = []

    if not Path(filename).is_file():
        raise FileNotFoundError("Data file '{}' missing".format(filename))

    try:
        with open(filename, 'r') as f:
            rows = json.load(f)

        for row in rows:
            # Typecast!!!!!!!
            key = str(row['id'])

            if (wanted_id is not None and key == wanted_id) or (wanted_id is None):
                product = {}
                for k,v in row.items():
                    product[k] = v
                data.append(product)

    except ValueError as exc:
        raise ValueError("Unable to load data from file '{}'".format(filename)) from exc

    return data

def load_csv_data(filename, wanted_id = None):
    """ Load JSON data from file and returns as dictionary """

    data = []

    if not Path(filename).is_file():
        raise FileNotFoundError("Data file '{}' missing".format(filename))

    try:
        with open(filename, 'r') as csvfile:
            # using DictReader method to convert each row to a dictionary
            for row in csv.DictReader(csvfile):
                if (wanted_id is not None and row['id'] == wanted_id) or (wanted_id is None):
                    data.append(row)
    except ValueError as exc:
        raise ValueError("Unable to load data from file '{}'".format(filename)) from exc

    return data

def load_sql_data(filename, wanted_id = None):
    """ Load SQLite data and return as dictionary """

    data = []
    where_clause = ""
    if wanted_id is not None:
        where_clause = " WHERE id = " + wanted_id

    con = sqlite3.connect(filename)
    cur = con.cursor()
    res = cur.execute("SELECT * FROM products " + where_clause)
    rows = res.fetchall()

    # longwinded way to get a list of the col names programatically
    keys = []
    colnames = cur.description
    for desc in colnames:
        keys.append(desc[0])

    # keys = ["id", "name", "category", "price"]
    for row_tuple in rows:
        item = {}
        i = 0
        for v in row_tuple:
            item[keys[i]] = v
            i = i + 1
        data.append(item)

    # print(data)

    return data

def create_sql_data(filename):
    """ Create SQLite data file if it doesn't already exist """

    con = sqlite3.connect(filename)
    cur = con.cursor()
    cur.execute("CREATE TABLE products(id, name, category, price)")
    cur.execute("""
        INSERT INTO products VALUES
            (1, "Laptop", "Electronics", 799.99),
            (2, "Coffee Mug", "Home Goods", 15.99)
    """)
    con.commit()


# Set debug=True for the server to auto-reload when there are changes
if __name__ == '__main__':
    app.run(host='localhost', port=5000, debug=True)
