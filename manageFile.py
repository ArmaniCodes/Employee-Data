from Modules import sqlite3, os

def get_all_employees_sorted_sql(sort_by_column):
    #connect to the SQLite database
    conn = sqlite3.connect('employee_data.db')
    cur = conn.cursor()

    # Validate the sort_by_column to prevent any Errors
    allowed_columns = ['salary', 'employee_id', 'name']
    if sort_by_column not in allowed_columns:
        raise ValueError("Invalid column for sorting.")

    # execute query
    query = f'''
                SELECT * FROM employees
                ORDER BY {sort_by_column}
            '''
    cur.execute(query)

    # fetch all results
    sorted_results = cur.fetchall()

    # close the connection
    conn.close()

    return sorted_results

def delete_employee_by_id(employee_id):
    # Connect to SQLite database
    conn = sqlite3.connect('employee_data.db')
    cur = conn.cursor()

    # Execute the DELETE query
    cur.execute('''
            DELETE FROM employees WHERE employee_id = ?
        ''', (employee_id,))

    #commit the changes and close the connection
    conn.commit()
    conn.close()

def search_employee_by_id(employee_id):
    #Connect to DB
    conn = sqlite3.connect('employee_data.db')
    cur = conn.cursor()
    cur.execute('''
                SELECT * FROM employees WHERE employee_id = ?
            ''', (employee_id,))

    #close connection to local db and return results
    result = cur.fetchone()
    conn.close()
    return result

def getEmployeeList():
    #Connect to DB
    conn = sqlite3.connect('employee_data.db')
    cur = conn.cursor()

    #Retrieve full employee list
    cur.execute('''
              SELECT * FROM employees
          ''')
    results = cur.fetchall()

    #Close connection and return
    conn.close()
    return results

def update_employee_data(employee_name,new_data):
    # Connect to SQLite database
    conn = sqlite3.connect('employee_data.db')
    cur = conn.cursor()

    rows_modified = cur.execute('''
            UPDATE employees
            SET 
                date_of_birth = ?,
                sex = ?,
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
        'Date Of Birth', 'Sex', 'Race', 'Email', 'Phone', 'Address',
        'Employee ID', 'Job Title', 'Department', 'Manager/Leader', 'Status',
        'Salary', 'Time and Attendance', 'Certifications and Skills', 'Training/Programs',
        'Extra Information', 'Age'
    ]

    employee_values = tuple(data[name][key] for key in keys_order)
    return employee_values

def createTable():
    # Connection to local db
    conn = sqlite3.connect('employee_data.db')
    cur = conn.cursor()

    # Creates Table if not already existing
    cur.execute('''
               CREATE TABLE IF NOT EXISTS employees (
                   id INTEGER PRIMARY KEY,
                   name TEXT,
                   date_of_birth TEXT,
                   sex TEXT,
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
    # Close Connection
    conn.commit()
    conn.close()

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
               sex TEXT,
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
                name, date_of_birth, sex, race, email, phone, address,
                employee_id, job_title, department, manager_leader, status, salary,
                time_and_attendance, certifications_skills, training_programs,
                extra_information, age
            ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
        ''', (name,) + formatData(data, name))


    #Close Connection
    conn.commit()
    conn.close()