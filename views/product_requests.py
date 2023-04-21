import sqlite3
from models import Product

PRODUCTS = [
    {
        "id": 1,
        "name": "Large Coffee",
        "price": 6.00
    },
    {
        "id": 2,
        "name": "Latte",
        "price": 8.99
    },
    {
        "id": 3,
        "name": "Espresso",
        "price": 11.80
    },
    {
        "id": 4,
        "name": "Americano",
        "price": 11.00
    },
    {
        "id": 5,
        "name": "Cubano",
        "price": 14.99
    },
    {
        "id": 6,
        "name": "Cappuccino",
        "price": 12.49
    }
]

def get_all_products():
    """Get all products."""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.name,
            p.price
        FROM Product p
        """)

        products = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            product = Product(row['id'], row['name'], row['price'])

            products.append(product.__dict__)

    return products

def get_single_product(id):
    """Get single product."""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.name,
            p.price
        FROM Product p
        WHERE p.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        product = Product(data['id'], data['name'], data['price'],)

        return product.__dict__

def get_product_by_price(price):
    """Code for getting order by price filtering"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            p.id,
            p.name,
            p.price
        FROM Product p
        WHERE p.price < ?
        """, ( price, ))

        products = []

        dataset = db_cursor.fetchall()

        for row in dataset:
            product = Product(row['id'], row['name'], row['price'])
            products.append(product.__dict__)

    return products

def create_product(new_product):
    """Create a new product"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Product
            ( name, price )
        VALUES
            ( ?, ? );
        """, (new_product['name'], new_product['price'], ))

        id = db_cursor.lastrowid
        new_product['id'] = id
    
    return new_product

def delete_product(id):
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Product
        WHERE id = ?
        """, ( id, ))

def update_product(id, new_product):
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Product
            SET
                name = ?,
                price = ?
        WHERE id = ?
        """, (new_product['name'], new_product['price'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True
