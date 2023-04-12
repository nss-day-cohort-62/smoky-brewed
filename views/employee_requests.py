EMPLOYEES = [
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
]

def get_all_employees():
    """Get all employees."""
    return EMPLOYEES

def get_single_employee(id):
    """Get single employee"""
    requested_employee = None

    for employee in EMPLOYEES:
        if employee["id"] == id:
            requested_employee = employee

    return requested_employee
