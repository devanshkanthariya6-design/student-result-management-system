<<<<<<< HEAD
<!-- issues -->
<!-- “What else did you do apart from CRUD?”

That’s where you should talk about:

UNIQUE constraints
UPSERT logic
Handling duplicate entries
Database normalization
Validation -->

<!-- “In my Student Result Management System project, I faced an issue where duplicate marks entries were being created for the same student and subject every time marks were submitted.

After debugging, I found that the root cause was in the database design — there was no constraint to prevent duplicate combinations of student_id and subject_id, so every form submission was inserting a new row instead of updating the existing one.

To solve this, I added a composite UNIQUE constraint on (student_id, subject_id) in the MySQL marks table. Then I used MySQL’s UPSERT functionality (ON DUPLICATE KEY UPDATE) in my Flask backend so that if a record already existed, it would update the marks instead of creating a new entry.

After this fix, the system started maintaining data consistency, and duplicate entries were completely eliminated.”
“I learned that data integrity should be enforced at the database level using constraints, not only in application logic.” -->




<!-- “In my Student Result Management System project, I faced a data duplication issue where the same student record and marks were being inserted multiple times when the form was submitted again.

After debugging, I realized the root cause was that there was no proper enforcement at the database level for uniqueness in some cases, and my initial insert logic was always creating new rows instead of checking existing data.

To solve this, I first added a UNIQUE constraint on the roll_no column in the students table to ensure that each student is uniquely identified. Then I improved my backend logic by using MySQL UPSERT (ON DUPLICATE KEY UPDATE) so that if a student already exists, their details get updated instead of creating duplicate entries.

Similarly, for the marks table, I used a composite UNIQUE key on (student_id, subject_id) to prevent duplicate marks entries and ensured consistency using UPSERT logic.

After implementing these changes, the system started maintaining proper data integrity and eliminated duplicate records completely.” -->





<!-- {% block content %} This fills the {% block content %} from base template-->
 <!--{% endblock %} Ends form and block-->


 <!-- Jinja templating : Template Inheritance : Other HTML files will extend this template They will fill this block with their content-->
<!--1. What is Jinja?

 Answer:

“Jinja is a templating engine used by Flask to render dynamic HTML.”

2. Why use base template?

 Answer:

“To avoid repeating common UI code across multiple pages.”

3. What is {% block %}?

 Answer:

“It defines a placeholder that child templates can override.”

4. Difference between {{ }} and {% %}?
{{ }} → output data
{% %} → logic (loops, blocks, conditions)-->

<!--An f-string (formatted string literal) is a concise and efficient way to embed variables and expressions directly into string literals in Python-->


<!-- # “I tested the backend independently by running the Flask server and verifying each route without building the frontend first.

# I inserted dummy data directly into MySQL tables like students, subjects, and marks.

# Then I created temporary test routes such as /students and /marks which returned raw data (like lists or JSON) instead of HTML.

# I opened these routes in the browser to check whether correct data was being fetched from the database.

# For relational data, I used JOIN queries and verified the output manually.

# I also used print statements and terminal logs to debug database connections and query results.

# This helped me ensure that all backend logic was working correctly before integrating it with the frontend.”
# “By doing this, I could isolate issues—if something failed, I knew it was either the route or database logic, not the UI.”
# “For example, I created a /students route that executed a SELECT query and returned the result directly. If I saw correct data in the browser, I knew the backend was working.”

# # Add Debug (VERY IMPORTANT)

# Inside any route:

# print(data)

# 👉 Check terminal:

# If data prints → backend working
# If error → fix query/connection

# Wrong login

# Test invalid credentials → should show error
# Quick Isolation Test (to check server is running)-- replace whole code with
# from flask import Flask
# app = Flask(__name__)

# @app.route('/')
# def home():
#     return "Working"

# if __name__ == '__main__':
#     app.run(debug=True)
# app = Flask(__name__) # app initialization | __name__ tells Flask: Where to find files
#    connects your frontend (HTML) with your backend (database functions).

# app.py
# Flask(Lightweight Python web framework)
# Used to create the main app
# render_template
# Used to send data to HTML pages
# request
# Used to get data from user (forms, input)
# redirect
# Redirect user to another route/page
# url_for(Avoid hardcoding URLs)
# Generates URL dynamically
# session (user interactions with a website or application that take place within a specific timeframe)
# Used to store user data (like login info) -->




<!-- (student_id,))  # execute function expects parameters as sequence (tuple or list) -->



<!-- /* box-sizing: border-box is a CSS property that changes how the browser calculates the total width and height of an element by including its padding and border within the specified dimensions. 
Key Differences
Default Behavior (content-box): If you set an element's width to 200px, the browser adds any padding and borders on top of that 200px, making the actual rendered box wider than intended.
Border-Box Behavior (border-box): If you set a width of 200px, that 200px is the final total width. If you add 20px of padding, the internal content area shrinks to accommodate it, but the overall box stays exactly 200px. */

/* CSS Flexbox Cheat Sheet (1-Page)
1. Enable Flexbox
display: flex;
2. Direction
flex-direction: row | column | row-reverse | column-reverse;
3. Main Axis (justify-content)
flex-start | flex-end | center | space-between | space-around | space-evenly;
4. Cross Axis (align-items)
stretch | flex-start | flex-end | center | baseline;
5. Wrap
flex-wrap: nowrap | wrap | wrap-reverse;
6. Align Content (multi-line)
flex-start | center | space-between | space-around;
7. Gap
gap | row-gap | column-gap;
8. Flex Item
flex-grow: 1;
flex-shrink: 1;
flex-basis: 200px;
flex: 1 1 200px;
9. Align Self
align-self: center | flex-start | flex-end;
10. Order
order: 0 (default);
11. Centering Trick
display: flex;
justify-content: center;
align-items: center;
Memory Tip: justify = main axis, align = cross axis */

/*overflow: hidden is a property value used to clip content that extends beyond the boundaries of its container, making the excess content invisible without providing scrollbars.*/
/*The text-decoration: none; property in CSS is primarily used to remove visual lines (underlines, overlines, or strike-throughs) from text. It is most commonly applied to anchor tags (<a>) to remove the default browser underline from hyperlinks.*/
/*What is Flexbox?
“A CSS layout system used to align elements efficiently.”*/



/*HTML (HyperText Markup Language)
HTML is used to structure the content of a webpage.
It defines elements like headings, paragraphs, images, links, tables, forms, etc.
It uses tags to organize content.

CSS (Cascading Style Sheets)
CSS is used to style and design the webpage.
It controls colors, layouts, fonts, spacing, animations, etc.
It makes the webpage visually appealing.*/ -->
=======
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
>>>>>>> 62173887ccf19d1a32dbe6eb9e939152381ed401
