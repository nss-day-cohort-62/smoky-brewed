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


def create_employee(employee):
    """Creates a new employee"""
    max_id = EMPLOYEES[-1]["id"]
    new_id = max_id + 1
    employee["id"] = new_id
    EMPLOYEES.append(employee)

    return employee


def update_employee(id, new_employee):
    """Updates employee info with client's replacement"""
    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            EMPLOYEES[index] = new_employee
            break


def delete_employee(id):
    """Deletes employee"""
    employee_index = None

    for index, employee in enumerate(EMPLOYEES):
        if employee["id"] == id:
            employee_index = index

    if employee_index is not None:
        EMPLOYEES.pop(employee_index)
