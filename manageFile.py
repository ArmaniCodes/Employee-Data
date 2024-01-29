from Modules import os
from Modules import json


def getEmployeeList():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'employee_data.json')

    #Return None if exception or file non-existing
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            try:
                data = json.load(file)
                return data
            except json.JSONDecodeError as e:
                return None
    else:
        return None


def checkIfEmployeeExist(name,empID):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'employee_data.json')

    #if theres no list then theres no possible way that employee already exist
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            loaded_employee_data = json.load(file)
    else:
        return name

    #If employee name already exist, we simply add the employee ID to the employees name to create a new Employee
    if name in loaded_employee_data:
        name = name + " " + empID
    return name

def saveToFile(employee_data):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'employee_data.json')

    #If it exist we update if not then we create
    if os.path.exists(file_path):
        with open(file_path, 'r') as file:
            loaded_employee_data = json.load(file)
    else:
        loaded_employee_data = employee_data
    loaded_employee_data.update(employee_data)
    with open(file_path, 'w') as file:
            json.dump(loaded_employee_data, file)