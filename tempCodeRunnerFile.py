# ── Enter Marks ────────────────────────────────────
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