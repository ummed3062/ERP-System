from flask import Flask, render_template, request,  redirect, url_for, flash, jsonify
import mysql.connector

app = Flask(__name__)

# Update the connection function to use MySQL
def get_db_connection():
    conn = mysql.connector.connect(
        host='localhost',
        user='root',          # MySQL user
        password='root',    # MySQL password
        database='erp_db'    # MySQL database
    )
    return conn

def create_table():
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS  lecture(
            lec_no INT AUTO_INCREMENT PRIMARY KEY,
            topic VARCHAR(100) NOT NULL,
            date VARCHAR(100) NOT NULL
        )
    ''')
    conn.commit()
    cursor.close()
    conn.close()

BTECH = [
    {'id': 1,
    'course': 'CSE-A',
     'semester': 5,
     'subject': 'python'},
    {'id': 2,
    'course': 'CSE-B',
    'semester': 5,
    'subject': 'python'},
    {'id': 3,
    'course': 'IT',
     'semester': 5,
     'subject': 'java'}
     
]


@app.route('/')
def home():
    return render_template('home.html', btech = BTECH)

@app.route('/api')
def home_json():
    return jsonify(BTECH)

@app.route('/courseplan')
def instruction_plan():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute('SELECT * FROM lecture')
    letures = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template('branch.html', letures= letures)


@app.route('/add', methods=('GET', 'POST'))
def add():
    if request.method == 'POST':
        lec_no = request.form['lec_no']
        topic = request.form['topic']
        date = request.form['date']

        if not lec_no or not topic or not date:
            flash('Lect. No., topic and date are required!')
        else:
            conn = get_db_connection()
            cursor = conn.cursor()
            cursor.execute('INSERT INTO lecture (lec_no, topic, date) VALUES (%s, %s, %s)', (lec_no, topic, date))
            conn.commit()
            cursor.close()
            conn.close()
            return redirect(url_for('instruction_plan'))

    return render_template('add.html')

if __name__ == '__main__':
    create_table()
    app.run(debug=True)