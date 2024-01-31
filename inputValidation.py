from Modules import *
from manageFile import search_employee_by_id, get_employee_data
from datetime import datetime

#When one of the check Methods returns false all will return false and result in data not being saved

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

def checkSex(data):
    gender = data["Gender"].get()
    if (gender != "M" and gender != "F"):
        #Prevent User from saving by returning False
        return False
    return True

#Validates status
def checkStatus(data):
    #Get text from the combobox
    status = data["Status"].get()
    if  (status != "Full Time" and status != "Part Time" and status != "Contract" and status != "Internship"):
        #Return false prevent user from saving
        return False
    return True


#Method to ensure that user is not supplying duplicate employee ID
def checkID(data):
    #Get entry instance and text
    emID = data["Employee ID"].get()
    ID_entry = data["Employee ID"]

    if search_employee_by_id(emID):
        #Warn user and return False to prevent saving
        ID_entry.delete(0, tb.END)
        ID_entry.insert(0, 'ERROR DUPLICATE ID ENTER NEW ONE')
        ID_entry.config(foreground='red')  # Set text color to black
        return False

    return True

#Method to ensure duplicate names are changed
def checkIfPersonExist(name, emID):
    if get_employee_data(name):
        name += " " + emID
    return name

# This method will call all other validation methods
def checkEntries(data):
    # We set retur to False if any fail so that if just one fails they all fail
    # But also to allow warnings to occur instead of just instantly returning upon one failure
    retur = True
    if not checkID(data):
        retur = False
    if not checkSex(data):
        retur = False
    if not checkStatus(data):
        retur = False
    if not checkBirthDate(data):
        retur = False
    if not checkSalary(data):
        retur = False
    return retur


#Input validate names
def cleanNames(phrase):
    newPhrase = ""
    for i in phrase:
        if i.isalnum():
            newPhrase += i
    return newPhrase

#Calculates employees age and returns it
def calculate_age(birthdate):
    today = datetime.today()
    birthdate = datetime.strptime(birthdate, '%m/%d/%Y')
    age = today.year - birthdate.year - ((today.month, today.day) < (birthdate.month, birthdate.day))
    return age

