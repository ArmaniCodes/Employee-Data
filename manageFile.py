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


def checkIfEmployeeExist(name,employee_data):
    pass