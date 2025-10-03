import psycopg2

# Database connection function
def get_connection():
    return psycopg2.connect(
        dbname="Employee_DB",      # your database name
        user="postgres",           # your username
        password="postgras",       # your password
        host="localhost",
        port="5432"
    )

# ---------------- CRUD OPERATIONS ---------------- #

# Create
def insert_employee():
    emp_company = input("Enter employee company: ")
    emp_technology = input("Enter employee technology: ")
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO employee (emp_company, emp_technology) VALUES (%s, %s)"
    cursor.execute(sql, (emp_company, emp_technology))
    conn.commit()
    print("Employee inserted successfully!")
    cursor.close()
    conn.close()

# Read
def fetch_employees():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM employee")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

# Update
def update_employee():
    emp_id = int(input("Enter employee ID to update: "))
    emp_company = input("Enter new company name: ")
    emp_technology = input("Enter new technology: ")
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE employee SET emp_company=%s, emp_technology=%s WHERE emp_id=%s"
    cursor.execute(sql, (emp_company, emp_technology, emp_id))
    conn.commit()
    print("Employee updated successfully!")
    cursor.close()
    conn.close()

# Delete
def delete_employee():
    emp_id = int(input("Enter employee ID to delete: "))
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM employee WHERE emp_id=%s"
    cursor.execute(sql, (emp_id,))
    conn.commit()
    print("Employee deleted successfully!")
    cursor.close()
    conn.close()

# ---------------- MENU-DRIVEN PROGRAM ---------------- #
if __name__ == "__main__":
    while True:
        print("\n--- Employee Management ---")
        print("1. Insert Employee")
        print("2. Show All Employees")
        print("3. Update Employee")
        print("4. Delete Employee")
        print("5. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            insert_employee()
        elif choice == "2":
            fetch_employees()
        elif choice == "3":
            update_employee()
        elif choice == "4":
            delete_employee()
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice! Please try again.")
