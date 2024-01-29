from modules import os
from modules import json


def getEmployeeList():
    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, 'employee_data.json')