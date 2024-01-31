from modules import *
from manageFile import search_employee_by_id, get_employee_data
from datetime import datetime


def checkBirthDate(data):
    #We try to retrieve the DOB from the user input
    try:
        birthdate = datetime.strptime((data["Date Of Birth"].get()), '%m/%d/%Y')
    except:
        #We warn the user since the DOB supplied is invalid
        dobentry = data["Date Of Birth"]
        dobentry.delete(0, tb.END)
        dobentry.insert(0, 'mm/dd/yyyy')
        dobentry.config(foreground='red')
        return False

    #Else return True
    return True

def checkSalary(data):
    #Get button instance and button text
    button = data["Salary"]
    salary = data["Salary"].get()

    #Input validate salary
    if salary is None or salary == '' or not (salary.isnumeric()):
        #Warn user since input is invalid and return False
        button.delete(0,tb.END)
        button.insert(0,'integer ONLY!')
        button.config(foreground='red')
        return False

    #else return True
    return True