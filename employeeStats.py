from Modules import sqlite3


def get_sex_counts():
    # Connect to db
    conn = sqlite3.connect('employee_data.db')
    cur = conn.cursor()

    cur.execute('''
           SELECT sex, COUNT(*) as count
           FROM employees
           GROUP BY sex
       ''')

    #Retrieve as dictionary
    sex_counts = dict(cur.fetchall())

    onn.close()

    return sex_counts

def get_employment_type_counts():
    #Connect to db
    conn = sqlite3.connect('employee_data.db')
    cur = conn.cursor()

    cur.execute('''
                   SELECT status, COUNT(*) as count
                   FROM employees
                   WHERE status IN ('Full Time', 'Part Time', 'Internship', 'Contract')
                   GROUP BY status
               ''')
    employment_type_counts = dict(cur.fetchall())
    return employment_type_counts


def get_all_salaries():
    pass