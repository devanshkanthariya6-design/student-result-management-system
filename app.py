
from flask import Flask, render_template, request, redirect, session, url_for
import database as db

app = Flask(__name__)
app.secret_key = 'devansh123'

# testing
# Test DB connection
@app.route('/test-db')
def test_db():
    conn = db.get_connection()
    return "DB Connected Successfully"

# Test students data

@app.route('/students-test')
def students_test():
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM students")
    data = cursor.fetchall()
    conn.close()
    return str(data)

# Test subjects

@app.route('/subjects-test')
def subjects_test():
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM subjects")
    data = cursor.fetchall()
    conn.close()
    return str(data)


@app.route('/marks-test')
def marks_test():
    conn = db.get_connection()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT s.name, sub.name, m.marks_obtained
        FROM marks m
        JOIN students s ON m.student_id = s.id
        JOIN subjects sub ON m.subject_id = sub.id
    """)

    data = cursor.fetchall()
    conn.close()

    return str(data)


# Login
@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        conn = db.get_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute(
            "SELECT * FROM admin WHERE username=%s AND password=%s",
            (username, password)
        )
        admin = cursor.fetchone()
        conn.close()
        if admin:
            session['logged_in'] = True
            return redirect('/dashboard')
        return render_template('login.html', error='Invalid credentials')
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.clear()
    return redirect('/')


# Dashboard 
@app.route('/dashboard')
def dashboard():
    if not session.get('logged_in'):
        return redirect('/')
    students = db.get_all_students()
    return render_template('dashboard.html', students=students,
                           total=len(students))


#  search student
@app.route('/search')
def search():
    if not session.get('logged_in'): return redirect('/')
    query = request.args.get('q', '')
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute(
        "SELECT * FROM students WHERE name LIKE %s OR roll_no LIKE %s",
        (f'%{query}%', f'%{query}%')
    )
    students = cursor.fetchall()
    conn.close()
    return render_template('dashboard.html', students=students, total=len(students))


#  Add Student 
@app.route('/add_student', methods=['GET', 'POST'])
def add_student():
    if not session.get('logged_in'): return redirect('/')
    if request.method == 'POST':
        db.add_student(request.form['roll_no'], request.form['name'],
                       request.form['branch'], request.form['year'])
        return redirect('/dashboard') # Prevents duplicate form submission
    return render_template('students.html')


#  Enter Marks 
@app.route('/marks/<int:student_id>', methods=['GET', 'POST'])
def add_marks(student_id):
    if not session.get('logged_in'): return redirect('/')
    conn = db.get_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM subjects")
    subjects = cursor.fetchall()
    if request.method == 'POST':
        for subject in subjects:
            marks = request.form.get(f"marks_{subject['id']}")
            if marks:
                cursor.execute(
                    "INSERT INTO marks (student_id, subject_id, marks_obtained) VALUES (%s,%s,%s) "
                    "ON DUPLICATE KEY UPDATE marks_obtained=%s",
                    (student_id, subject['id'], marks, marks)
                )
        conn.commit()
        conn.close()
        return redirect(f'/result/{student_id}')
    conn.close()
    return render_template('add_marks.html', subjects=subjects,
                           student_id=student_id)


#  delete student
@app.route('/delete/<int:student_id>')
def delete_student(student_id):
    if not session.get('logged_in'): return redirect('/')
    conn = db.get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM marks WHERE student_id = %s", (student_id,))  # safety net
    cursor.execute("DELETE FROM students WHERE id = %s", (student_id,))
    conn.commit()
    conn.close()
    return redirect('/dashboard')


#  Result Page 
@app.route('/result/<int:student_id>')
def result(student_id):
    if not session.get('logged_in'): return redirect('/')
    rows = db.get_student_result(student_id)
    if not rows:
        return "No result found", 404
    total = sum(r['marks_obtained'] for r in rows)
    max_total = sum(r['max_marks'] for r in rows)
    percentage = round((total / max_total) * 100, 2)
    grade = db.get_grade(percentage)
    passed = all(r['marks_obtained'] >= 35 for r in rows)
    return render_template('result.html', rows=rows,
                           student=rows[0], total=total,
                           max_total=max_total,
                           percentage=percentage,
                           grade=grade, passed=passed)

if __name__ == '__main__':
    app.run(debug=True)
