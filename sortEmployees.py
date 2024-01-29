from editEmployeeGUI import employeeInfoWdw
from manageFile import getEmployeeList

def searchForEmployee(root,guiInstance,name):
    empList = getEmployeeList()
    #If emply exist then we can call employeeInfoWdw which will load the data visually and allow us to edit it
    if name in empList:
        employeeInfoWdw(root,name,guiInstance)

def sortByName():
    data = getEmployeeList()
    if data:
        sorted_data = dict(sorted(data.items()))

def sortByID():
    pass
