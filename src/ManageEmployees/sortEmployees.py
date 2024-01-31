from src.GUIS.editEmployeeGUI import employeeInfoWdw
from src.ManageEmployees.manageFile import get_employee_data, get_all_employees_sorted_sql

def searchForEmployee(root,guiInstance,name):
    if get_employee_data(name):
        employeeInfoWdw(root, name, guiInstance)

def sortByName(LoadEmployeesMethod):
    data = get_all_employees_sorted_sql("name")
    if data:
        LoadEmployeesMethod(data)

def sortByID(LoadEmployeesMethod):
    data = get_all_employees_sorted_sql("employee_id")
    if data:
        LoadEmployeesMethod(data)

def sortBySalary(LoadEmployeesFunction):
    data = get_all_employees_sorted_sql("salary")
    if data:
        LoadEmployeesFunction(data)