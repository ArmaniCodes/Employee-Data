from Modules import sqlite3


def addEmployee(data,name):
    #Connection to local db
    conn = sqlite3.connect('employee_data.db')
    cur = conn.cursor()

    # Creates Table if not already existing
    cur.execute('''
           CREATE TABLE IF NOT EXISTS employees (
               id INTEGER PRIMARY KEY,
               name TEXT,
               date_of_birth TEXT,
               gender TEXT,
               race TEXT,
               email TEXT,
               phone TEXT,
               address TEXT,
               employee_id TEXT,
               job_title TEXT,
               department TEXT,
               manager_leader TEXT,
               status TEXT,
               salary INTEGER,
               time_and_attendance TEXT,
               certifications_skills TEXT,
               training_programs TEXT,
               extra_information TEXT,
               age INTEGER
           )
       ''')

    cur.execute('''
            INSERT INTO employees (
                name, date_of_birth, gender, race, email, phone, address,
                employee_id, job_title, department, manager_leader, status, salary,
                time_and_attendance, certifications_skills, training_programs,
                extra_information, age
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
        ''', (name,) + formatData(data, name))