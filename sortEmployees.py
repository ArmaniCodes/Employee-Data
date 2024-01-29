from editEmployeeGUI import employeeInfoWdw
from manageFile import getEmployeeList

def searchForEmployee(root,guiInstance,name):
    empList = getEmployeeList()
    #If emply exist then we can call employeeInfoWdw which will load the data visually and allow us to edit it
    if name in empList:
        employeeInfoWdw(root,name,guiInstance)

def sortByName(LoadEmployeesMethod):
    data = getEmployeeList()
    if data:
        sorted_data = dict(sorted(data.items()))
        LoadEmployeesMethod(sorted_data)

def sortByID(LoadEmployeesMethod):
    data = getEmployeeList()
    if data:
        sorted_data = dict(sorted(data.items(), key=lambda x: int(x[1]["Employee ID"])))
        LoadEmployeesMethod(sorted_data)

def sortBySalary(LoadEmployeesFunction):
    data = getEmployeeList()
    if data:
        sorted_data = dict(sorted(data.items(), key=lambda x: int(x[1]["Salary"]), reverse=True))
        LoadEmployeesFunction(sorted_data)