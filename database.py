#  all database function 



import mysql.connector    
def get_connection():
    return mysql.connector.connect(  
        host="localhost",
        user="root", 
        password="Pomn@0987",
        database="student_db"
    )


def get_all_students(): 
    conn = get_connection()  
    cursor = conn.cursor(dictionary=True)  
    cursor.execute("SELECT * FROM students ORDER BY roll_no")
    result = cursor.fetchall()  
    conn.close()  
    return result


def add_student(roll_no, name, branch, year):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """INSERT INTO students (roll_no, name, branch, year) VALUES (%s,%s,%s,%s)
        ON DUPLICATE KEY UPDATE
        name = VALUES(name),
        branch = VALUES(branch),
        year = VALUES(year)
        """,
        (roll_no, name, branch, year)
    )
    conn.commit() 
    conn.close()


def get_student_result(student_id):
    conn = get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("""
        SELECT s.name, s.roll_no, sub.name AS subject,
               m.marks_obtained, sub.max_marks
        FROM students s
        JOIN marks m ON s.id = m.student_id
        JOIN subjects sub ON m.subject_id = sub.id
        WHERE s.id = %s
    """, (student_id,))  
    rows = cursor.fetchall()
    conn.close()
    return rows

def get_grade(percentage):
    if percentage >= 90: return 'A'
    elif percentage >= 75: return 'B'
    elif percentage >= 60: return 'C'
    elif percentage >= 50: return 'D'
    else: return 'F'