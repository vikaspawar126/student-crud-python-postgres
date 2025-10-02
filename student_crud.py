import psycopg2

# Database connection
def get_connection():
    return psycopg2.connect(
        dbname="Test3",
        user="postgres",
        password="postgras",
        host="localhost",
        port="5432"
    )

# Create
def insert_student(name, age, email):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "INSERT INTO student (name, age, email) VALUES (%s, %s, %s)"
    cursor.execute(sql, (name, age, email))
    conn.commit()
    print("✅ Student inserted successfully.")
    cursor.close()
    conn.close()

# Read
def fetch_students():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM student")
    rows = cursor.fetchall()
    print("\n📋 Student Records:")
    for row in rows:
        print(row)
    cursor.close()
    conn.close()

# Update
def update_student(student_id, name, age, email):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "UPDATE student SET name=%s, age=%s, email=%s WHERE id=%s"
    cursor.execute(sql, (name, age, email, student_id))
    conn.commit()
    print("✅ Student updated successfully.")
    cursor.close()
    conn.close()

# Delete
def delete_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    sql = "DELETE FROM student WHERE id=%s"
    cursor.execute(sql, (student_id,))
    conn.commit()
    print("✅ Student deleted successfully.")
    cursor.close()
    conn.close()

# Menu
if __name__ == "__main__":
    while True:
        print("\nCRUD Operations:")
        print("1. Insert Student")
        print("2. Show Students")
        print("3. Update Student")
        print("4. Delete Student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            age = int(input("Enter age: "))
            email = input("Enter email: ")
            insert_student(name, age, email)

        elif choice == "2":
            fetch_students()

        elif choice == "3":
            student_id = int(input("Enter student ID to update: "))
            name = input("Enter new name: ")
            age = int(input("Enter new age: "))
            email = input("Enter new email: ")
            update_student(student_id, name, age, email)

        elif choice == "4":
            student_id = int(input("Enter student ID to delete: "))
            delete_student(student_id)

        elif choice == "5":
            print("Exiting program... 👋")
            break

        else:
            print("❌ Invalid choice, try again!")
            