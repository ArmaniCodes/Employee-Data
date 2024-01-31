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