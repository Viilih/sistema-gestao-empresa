from database.database import get_db_connection

class Employee:
    def __init__(self, emp_id, name, age, position, team_id):
        self.id = emp_id
        self.name = name
        self.age = age
        self.position = position
        self.team_id = team_id

    
    def add(name, age, position, team_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("INSERT INTO employees (name, age, position, team_id) VALUES (?, ?, ?, ?)",
                           (name, age, position, team_id))
            conn.commit()
        except Exception as e:
            print(f"Error adding employee: {e}")
        finally:
            conn.close()

    
    def update(emp_id, name, age, position, team_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("UPDATE employees SET name = ?, age = ?, position = ?, team_id = ? WHERE id = ?",
                           (name, age, position, team_id, emp_id))
            conn.commit()
        except Exception as e:
            print(f"Error updating employee: {e}")
        finally:
            conn.close()

    
    def delete(emp_id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("DELETE FROM employees WHERE id = ?", (emp_id,))
            conn.commit()
        except Exception as e:
            print(f"Error deleting employee: {e}")
        finally:
            conn.close()

    
    def get_all():
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employees")
            employees = cursor.fetchall()
            return employees
        except Exception as e:
            print(f"Error getting all employees: {e}")
            return None
        finally:
            conn.close()

    
    def get_employee_by_id(id):
        try:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM employees WHERE id = ?", (id,))
            employee = cursor.fetchone()
            return employee
        except Exception as e:
            print(f"Error getting employee by ID: {e}")
            return None
        finally:
            conn.close()
