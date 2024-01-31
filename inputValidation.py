from modules import *
from manageFile import search_employee_by_id, get_employee_data
from datetime import datetime


def checkBirthDate(data):
    try:
        birthdate = datetime.strptime((data["Date Of Birth"].get()), '%m/%d/%Y')
    except:
        dobentry = data["Date Of Birth"]
        dobentry.delete(0, tb.END)
        dobentry.insert(0, 'mm/dd/yyyy')
        dobentry.config(foreground='red')
        return False
    return True