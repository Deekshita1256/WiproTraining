import pymysql

class EmployeeDB:
    def __init__(self):
        try:
            self.conn = pymysql.connect(
                host="localhost",
                user="root",
                password="pass@word1",
                database="employeedb"
            )
            self.cursor = self.conn.cursor()
            print("Database connection established!")
        except pymysql.MySQLError as e:
            print(f"Error connecting to MySQL: {e}")
            raise

    # CREATE
    def create_employee(self, emp_id, name, salary):
        try:
            self.cursor.execute(
                "INSERT INTO employee (id, name, salary) VALUES (%s, %s, %s)",
                (emp_id, name, salary)
            )
            self.conn.commit()
            print(f"Employee '{name}' created successfully.")
        except pymysql.MySQLError as e:
            print(f"Error creating employee: {e}")

    # READ
    def read_employees(self):
        try:
            self.cursor.execute("SELECT * FROM employee")
            rows = self.cursor.fetchall()
            if not rows:
                print("No employees found.")
            for row in rows:
                print(row)
        except pymysql.MySQLError as e:
            print(f"Error reading employees: {e}")

    # UPDATE
    def update_employee(self, emp_id, new_salary):
        try:
            self.cursor.execute(
                "UPDATE employee SET salary=%s WHERE id=%s",
                (new_salary, emp_id)
            )
            self.conn.commit()
            print(f"Employee ID {emp_id} updated successfully.")
        except pymysql.MySQLError as e:
            print(f"Error updating employee: {e}")

    # DELETE
    def delete_employee(self, emp_id):
        try:
            self.cursor.execute(
                "DELETE FROM employee WHERE id=%s",
                (emp_id,)
            )
            self.conn.commit()
            print(f"Employee ID {emp_id} deleted successfully.")
        except pymysql.MySQLError as e:
            print(f"Error deleting employee: {e}")

    # Close connection
    def close(self):
        self.cursor.close()
        self.conn.close()
        print("Database connection closed.")

# ============================
# Example Usage
# ============================

if __name__ == "__main__":
    db = EmployeeDB()

    # CREATE
    db.create_employee(1, "Alice", 50000)
    db.create_employee(2, "Bob", 55000)

    # READ
    print("\nAll Employees:")
    db.read_employees()

    # UPDATE
    db.update_employee(1, 60000)
    print("\nAfter Update:")
    db.read_employees()

    # DELETE
    db.delete_employee(2)
    print("\nAfter Delete:")
    db.read_employees()

    # Close connection
    db.close()