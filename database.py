import sqlite3

def create_database():
    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    cursor.execute('''
        CREATE TABLE IF NOT EXISTS students (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            total_marks INTEGER,
            age INTEGER,
            grade TEXT
        )
    ''')

    conn.commit()
    cursor.close()
    conn.close()

def populate_database():
    students = [
    ('John Smith', 80, 18, 'A'),
    ('Emma Johnson', 92, 17, 'A'),
    ('Michael Davis', 75, 19, 'B'),
    ('Sophia Anderson', 88, 18, 'B'),
    ('Ethan Brown', 95, 17, 'A'),
    ('Olivia Wilson', 82, 19, 'B'),
    ('William Thomas', 78, 18, 'B'),
    ('Ava Lee', 90, 17, 'A'),
    ('James Miller', 85, 19, 'A'),
    ('Isabella Clark', 93, 18, 'A'),
    ('Subhash Dixit', 98, 23, 'A'),
    ('Tom Holland', 55, 16, 'C'),
    ('Robert DJ', 75, 19, 'B'),
    ('Chris Evans', 88, 18, 'B'),
    ('Chris Hemsworth', 95, 17, 'A'),
    ('John Smith', 73, 22, 'A'),
    ('Mary Jones', 64, 25, 'B'),
    ('Michael Brown', 55, 28, 'A'),
    ('Sarah Green', 46, 31, 'B'),
    ('David Williams', 37, 34, 'A'),
    ('Emily Taylor', 28, 37, 'B'),
    ('Thomas Anderson', 19, 40, 'A'),
    ('Jennifer White', 10, 43, 'B'),
    ('Kevin Walker', 1, 46, 'A'),
    ('Susan Brown', 81, 18, 'B'),
    ('James Smith', 72, 21, 'A'),
    ('Nancy Jones', 63, 24, 'B'),
    ('Peter Green', 54, 27, 'A'),
    ('Lisa Williams', 45, 30, 'B'),
    ('William Taylor', 36, 33, 'A'),
    ('Carol Anderson', 27, 36, 'B'),
    ('Christopher White', 18, 39, 'A'),
    ('Daniel Walker', 9, 42, 'B'),
    ('Andrew Brown', 80, 17, 'A'),
    ('Jessica Smith', 71, 20, 'B'),
    ('Michael Jones', 62, 23, 'A'),
    ('Sarah Green', 53, 26, 'B'),
    ('David Williams', 44, 29, 'A'),
    ('Emily Taylor', 35, 32, 'B'),
    ('Thomas Anderson', 26, 35, 'A'),
    ('Jennifer White', 17, 38, 'B'),
    ('Kevin Walker', 8, 41, 'A'),
    ('Susan Brown', 79, 16, 'B'),
    ('James Smith', 70, 19, 'A'),
    ('Nancy Jones', 61, 22, 'B'),
    ('Peter Green', 52, 25, 'A'),
    ('Lisa Williams', 43, 28, 'B'),
    ('William Taylor', 34, 31, 'A'),
    ('Carol Anderson', 25, 34, 'B'),
    ('Christopher White', 16, 37, 'A'),
    ('Daniel Walker', 7, 40, 'B'),
    ('Andrew Brown', 78, 15, 'A'),
    ('Jessica Smith', 69, 18, 'B'),
    ('Michael Jones', 60, 21, 'A'),
    ('Sarah Green', 51, 24, 'B'),
    ('David Williams', 42, 27, 'A'),
    ('Emily Taylor', 33, 30, 'B'),
    ('Thomas Anderson', 24, 33, 'A'),
    ('Jennifer White', 15, 36, 'B'),
    ('Kevin Walker', 6, 39, 'A'),
    ('Susan Brown', 77, 14, 'B'),
    ('James Smith', 68, 17, 'A'),
    ('Nancy Jones', 59, 20, 'B'),
    ('Peter Green', 50, 23, 'A'),
    ('Lisa Williams', 41, 26, 'B'),
    ('William Taylor', 32, 29, 'A'),
    ('Carol Anderson', 23, 32, 'B'),
    ('Christopher White', 14, 35, 'A'),
    ('Daniel Walker', 5, 38, 'B')
    ]

    conn = sqlite3.connect('student.db')
    cursor = conn.cursor()

    cursor.executemany('''
        INSERT INTO students (name, total_marks, age, grade) 
        VALUES (?, ?, ?, ?)
    ''', students)

    conn.commit()
    cursor.close()
    conn.close()

if __name__ == '__main__':
    create_database()
    populate_database()