import sqlite3
from models import Order
from .product_requests import get_single_product
from .employee_requests import get_single_employee

ORDERS = [
    {
        "id": 1, "product_id": 6, "employee_id": 3, "timestamp": 1613538111396
    }, {
        "id": 2, "product_id": 5, "employee_id": 1, "timestamp": 1613038102396
    }, {
        "id": 3, "product_id": 2, "employee_id": 2, "timestamp": 1612837112396
    }, {
        "id": 4, "product_id": 1, "employee_id": 4, "timestamp": 1612836112396
    }, {
        "id": 5, "product_id": 4, "employee_id": 3, "timestamp": 1612735112396
    },
]

def get_all_orders():
    """Get all orders using SQL database."""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
        o.id,
        o.product_id,
        o.employee_id,
        o.timestamp
    From "Order" o
        """)

    orders = []
    dataset = db_cursor.fetchall()

    for row in dataset:
        order = Order(row['id'], row['product_id'], row['employee_id'], row['timestamp'],)

        orders.append(order.__dict__)

    return ORDERS


def get_single_order(id):
    """Get single order from SQL."""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
        o.id,
        o.product_id,
        o.employee_id,
        o.timestamp
    From "Order" o
    WHERE o.id = ?
        """, ( id, ))

    data = db_cursor.fetchone()

    order = Order(data['id'], data['product_id'], data['employee_id'], data['timestamp'],)

    return order.__dict__


def create_order(order):
    """Creates a new order"""
    max_id = ORDERS[-1]["id"]
    new_id = max_id + 1
    order["id"] = new_id
    ORDERS.append(order)
    return order

def update_order(id, new_order):
    """Edit Order."""
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            ORDERS[index] = new_order
            break

def delete_order(id):
    """To Delete Order"""
    order_index = -1
    for index, order in enumerate(ORDERS):
        if order["id"] == id:
            order_index = index
    if order_index >= 0:
        ORDERS.pop(order_index)
