DATABASE = {
    "employees": [
        {
            "id": 1,
            "name": "Dylan Kline",
            "email": "dylan@kline.com",
            "hourly_rate": 18.25
        },
        {
            "id": 2,
            "name": "Ernie Fabian",
            "email": "ernie@fabian.com",
            "hourly_rate": 21.50
        },
        {
            "id": 3,
            "name": "Emeka Akoma",
            "email": "emeka@akoma.com",
            "hourly_rate": 18.75
        },
        {
            "id": 4,
            "name": "Jessalynn Whyte",
            "email": "jess@whyte.com",
            "hourly_rate": 19.75
        },
    ],
    "products": [
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
    ],
    "orders": [
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
}


def all(resource):
    """For GET requests to collection"""
    return DATABASE[resource]


def retrieve(resource, id):
    """For GET requests to a single resource"""
    requested_resource = None
    for item in DATABASE[resource]:
        if item["id"] == id:
            requested_resource = item

    return requested_resource


def create(resource, post_body):
    """For POST requests to a collection"""
    max_id = DATABASE[resource][-1]["id"]
    new_id = max_id + 1
    post_body["id"] = new_id
    DATABASE[resource].append(post_body)

    return post_body


def update(resource, id, post_body):
    """For PUT requests to a single resource"""
    for index, item in enumerate(DATABASE[resource]):
        if item["id"] == id:
            DATABASE[resource][index] = post_body
            break


def delete(resource, id):
    """For DELETE requests to a single resource"""
    resource_index = None
    for index, item in enumerate(DATABASE[resource]):
        if item["id"] == id:
            resource_index = index

    if resource_index is not None:
        DATABASE[resource].pop(resource_index)
