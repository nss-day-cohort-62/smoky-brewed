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
        "name": "Cappucino",
        "price": 12.49
    }
]

def get_all_products():
    """Get all products."""
    return PRODUCTS

def get_single_product(id):
    """Get single product."""
    requested_product = None

    for product in PRODUCTS:
        if product["id"] == id:
            requested_product = product

    return requested_product


