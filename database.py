import mysql.connector

# MySQL connection configuration
db_config = {
    'host': 'localhost',
    'user': 'admin',
    'password': '123456',
    'database': 'result_management'
}

# Connect to MySQL
conn = mysql.connector.connect(**db_config)
cursor = conn.cursor()

def create_student(name, marks):
    query = 'INSERT INTO students (name, marks) VALUES (%s, %s)'
    cursor.execute(query, (name, marks))
    conn.commit()

def get_students():
    query = 'SELECT * FROM students'
    cursor.execute(query)
    return cursor.fetchall()

def get_student_by_id(student_id):
    query = 'SELECT * FROM students WHERE id = %s'
    cursor.execute(query, (student_id,))
    return cursor.fetchone()

def update_student_result(student_id, marks):
    query = 'UPDATE students SET marks = %s WHERE id = %s'
    cursor.execute(query, (marks, student_id))
    conn.commit()