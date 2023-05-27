from flask import Flask, request, jsonify, render_template
import sqlite3

app = Flask(__name__)
app.config['JSON_SORT_KEYS'] = False


@app.route('/', methods=['GET'])
def get_students():
    page = request.args.get('page')
    if page is None or not page.isdigit():
        page = 1
    else:
        page = int(page)

    page_size = int(request.args.get('page_size', 10))
    offset = (page - 1) * page_size

    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    query = 'SELECT * FROM students WHERE 1=1'
    params = []

    criteria = request.args.get('criteria')
    if criteria:
        criteria = eval(criteria)
        if 'name' in criteria:
            query += ' AND name LIKE ?'
            params.append(f"%{criteria['name']}%")

        if 'total_marks' in criteria:
            query += ' AND total_marks >= ?'
            params.append(criteria['total_marks'])


    query += f' LIMIT {page_size} OFFSET {offset}'
    cursor.execute(query, params)
    filtered_students = cursor.fetchall()

    total_count = len(filtered_students)

    students = []
    for row in filtered_students:
        student = {
            'id': row[0],
            'name': row[1],
            'total_marks': row[2],
            'age': row[3],
            'grade': row[4]
        }
        students.append(student)

    cursor.close()
    conn.close()

    return render_template('index.html', students=students, total_count=total_count, page=page, page_size=page_size)