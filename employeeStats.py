import sqlite3


def get_sex_counts():
    # Connect to db
    conn = sqlite3.connect('employee_data.db')
    cur = conn.cursor()

    cur.execute('''
           SELECT gender, COUNT(*) as count
           FROM employees
           GROUP BY gender
       ''')

    #Retrieve as dictionary
    gender_counts = dict(cur.fetchall())

    onn.close()

    return gender_counts