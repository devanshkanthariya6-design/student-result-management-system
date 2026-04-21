# Student Result Management System

A web-based system to manage student records and results.

## Features
- Admin login with session management
- Add, view, delete students
- Enter subject-wise marks
- Auto-calculate percentage, grade (A/B/C/D/F), and pass/fail
- Search students by name or roll number
- Printable result card

## Tech Stack
- Backend: Python (Flask)
- Database: MySQL
- Frontend: HTML, CSS, Jinja2 Templates

## How to Run
1. Clone the repo: `git clone ...`
2. Install dependencies: `pip install flask mysql-connector-python`
3. Import `schema.sql` into MySQL
4. Run: `python app.py`
5. Open: `http://localhost:5000` (login: admin / admin123)
