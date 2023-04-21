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
            employee = Employee(row['id'], row['name'],
                                row['email'], row['hourly_rate'])

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
        """, (id, ))

        data = db_cursor.fetchone()

        employee = Employee(data['id'], data['name'],
                            data['email'], data['hourly_rate'])

        return employee.__dict__


def get_employees_by_name(name):
    """"Gets employees by searched name"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        conn.row_factory = sqlite3.Row
        db_cursor = conn.cursor()

        db_cursor.execute("""
        SELECT
            e.id,
            e.name,
            e.email,
            e.hourly_rate
        FROM Employee e
        WHERE e.name LIKE ?
        """, (f'%{name}%', ))

        employees = []
        dataset = db_cursor.fetchall()

        for row in dataset:
            employee = Employee(row['id'], row['name'],
                                row['email'], row['hourly_rate'])
            employees.append(employee.__dict__)

    return employees


def create_employee(new_employee):
    """Creates a new employee"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        INSERT INTO Employee
            ( name, email, hourly_rate )
        VALUES
            ( ?, ?, ? );
        """, (new_employee['name'], new_employee['email'],
              new_employee['hourly_rate'], ))

        id = db_cursor.lastrowid
        new_employee['id'] = id

    return new_employee


def update_employee(id, new_employee):
    """Updates employee info with client's replacement"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        UPDATE Employee
            SET
                name = ?,
                email = ?,
                hourly_rate = ?
        WHERE id = ?
        """, (new_employee['name'], new_employee['email'],
              new_employee['hourly_rate'], id, ))

        rows_affected = db_cursor.rowcount

    if rows_affected == 0:
        return False
    else:
        return True


def delete_employee(id):
    """Deletes employee"""
    with sqlite3.connect("./brewed.sqlite3") as conn:
        db_cursor = conn.cursor()

        db_cursor.execute("""
        DELETE FROM Employee
        WHERE id = ?
        """, (id, ))
