import sqlite3
from models import Employee

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
    """Get all employees"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()
        db_cursor.execute("""
            SELECT
                e.id,
                e.name,
                e.email,
                e.hourly_rate
            FROM `Employee` e
            """)
        
        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'], row['email'], row['hourly_rate'])

            employees.append(employee.__dict__)

    return employees

def get_single_employee(id):
    """Get single employee by id"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.email,
            e.hourly_rate
        FROM 'Employee' e
        WHERE e.id = ?
        """, ( id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'], data['email'], data['hourly_rate'])

        return employee.__dict__


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
