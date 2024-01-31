from Modules import sqlite3


def addEmployee(data,name):
    #Connection to local db
    conn = sqlite3.connect('employee_data.db')
    cur = conn.cursor()