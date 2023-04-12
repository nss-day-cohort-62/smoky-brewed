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
    """Get all orders."""
    return ORDERS


def get_single_order(id):
    """Get single order."""
    requested_order = None
    for order in ORDERS:
        if order["id"] == id:
            requested_order = order.copy()
            matching_product = get_single_product(
                requested_order["product_id"])
            requested_order.pop("product_id")
            requested_order["product"] = matching_product
            matching_employee = get_single_employee(
                requested_order["employee_id"])
            requested_order.pop("employee_id")
            requested_order["employee"] = matching_employee
    return requested_order
