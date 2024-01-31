from Modules import sqlite3



def update_employee_data(employee_name,new_data):
    # Connect to SQLite database
    conn = sqlite3.connect('employee_data.db')
    cur = conn.cursor()

    rows_modified = cur.execute('''
            UPDATE employees
            SET 
                date_of_birth = ?,
                gender = ?,
                race = ?,
                email = ?,
                phone = ?,
                address = ?,
                employee_id = ?,
                job_title = ?,
                department = ?,
                manager_leader = ?,
                status = ?,
                salary = ?,
                time_and_attendance = ?,
                certifications_skills = ?,
                training_programs = ?,
                extra_information = ?,
                age = ?
            WHERE name = ?
        ''', (*(formatData(new_data, employee_name)), employee_name)).rowcount
        #Unpack the returned tuple from formatData and update accordingly in the db
    conn.commit()
    conn.close()


def get_employee_data(employee_name):
    #Connect to local db
    conn = sqlite3.connect('employee_data.db')
    cur = conn.cursor()

    cur.execute('''
                SELECT * FROM employees WHERE name = ?
            ''', (employee_name,))

    result = cur.fetchone()
    conn.close()
    return result

#We need to format before adding to DB because the information is out of order
def formatData(data,name):
    #Order to enter the db
    keys_order = [
        'Date Of Birth', 'Gender', 'Race', 'Email', 'Phone', 'Address',
        'Employee ID', 'Job Title', 'Department', 'Manager/Leader', 'Status',
        'Salary', 'Time and Attendance', 'Certifications and Skills', 'Training/Programs',
        'Extra Information', 'Age'
    ]

    employee_values = tuple(data[name][key] for key in keys_order)
    return employee_values

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

    #Add employee to db
    cur.execute('''
            INSERT INTO employees (
                name, date_of_birth, gender, race, email, phone, address,
                employee_id, job_title, department, manager_leader, status, salary,
                time_and_attendance, certifications_skills, training_programs,
                extra_information, age
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
        ''', (name,) + formatData(data, name))


    #Close Connection
    conn.commit()
    conn.close()