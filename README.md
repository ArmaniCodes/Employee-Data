## Employee Data Manager
Manage employee data for thousands of employees while being able to retrieve statistics and visualize them with graphs. This program utilizes SQLite3 to store data locally. Tkinter is employed for displaying and allowing modification of employee data. Matplotlib is utilized to visually represent employee statistics through graphs, providing an insightful overview of the data.
As data is stored locally, it's important to note that this project is not intended for deployment in a real-world corporate environment, but it's a visually fun and great way to learn about SQL and GUIS.

## Features
```sh
1. Display and Individual Data Inspection:
    -  View a comprehensive list of all employees.
    -  Inspect individual employee data with ease.

2. Data Modification:
    -  Override existing employee data.
    -  Add new employees to the database.
    -  Delete unwanted employees.

3. Sorting and Searching Options:
    -  Sort employees by salary.
    -  Sort employees by employee ID.
    -  Sort employees alphabetically.
    -  Efficiently search employees by name.

4. Graphical Insights:
    -  Visualize the distribution of employees based on gender with a donut chart.
    -  Gain insights into the distribution of employment status with a donut chart.
    -  View a histogram depicting the salary distribution among employees.
    -  Explore the relationship between salary and age through a line chart.

5. Data validation:
    - Prevent duplicate users from existing
    - Users with same name can be differentiated by their Employee ID
    - Data will be validated before it is stored or used.
```

## Installation
Clone this repo
```sh
git clone "https://github.com/ArmaniCodes/employee-data-manager/"
```

## Dependencies
ttkbootstrap, matplotlib: To download simply run:
```sh
pip install -r requirements.txt
```

## Usage
Upon running you can create employees and fill their data up to then store in the local db. You can load previous databases, as well as delete,add,or display information.

## Screenshots
![image](https://github.com/ArmaniCodes/Employee-Data-Manager/assets/103855175/f8b0438f-8961-474a-a2c9-44e1ec66e639)

![image](https://github.com/ArmaniCodes/Employee-Data-Manager/assets/103855175/25a36ab6-d82d-44b8-be0d-b0eb0d47ab7e) ![image](https://github.com/ArmaniCodes/Employee-Data-Manager/assets/103855175/278df230-68d6-4f70-b793-7cdb700e79b8)

![image](https://github.com/ArmaniCodes/Employee-Data-Manager/assets/103855175/77c4ae64-0676-4232-a97e-c5e924e07a60)

![image](https://github.com/ArmaniCodes/Employee-Data-Manager/assets/103855175/b8720f6d-8883-43ba-9c19-1e41e443fed2)


