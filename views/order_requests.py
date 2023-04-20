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
        order = Order(row['id'], row['product_id'],
                      row['employee_id'], row['timestamp'],)

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
        """, (id, ))

    data = db_cursor.fetchone()

    order = Order(data['id'], data['product_id'],
                  data['employee_id'], data['timestamp'],)

    return order.__dict__


def create_order(new_order):
    """Creates a new order for SQL"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO "Order"
            ( product_id, employee_id, timestamp  )
        VALUES 
            (?,?,?);
        """, (new_order['product_id'], new_order['employee_id'], new_order['timestamp'],))

        id = db_cursor.lastrowid
        new_order['id'] = id
    return new_order


def update_order(id, new_order):
    """Update Order in SQL."""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE "Order"
            SET
                product_id = ?,
                employee_id = ?,
                timestamp = ?
            WHERE id = ?
        """, (new_order['product_id'], new_order['employee_id'], new_order['timestamp'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True


def delete_order(id):
    """To Delete Order from SQL"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM "order"
        WHERE id = ?
        """, (id, ))
