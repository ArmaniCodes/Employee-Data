from modules import *
from manageFile import getEmployeeList
from manageFile import saveToFile

def save(new_window,entryList,name):
    fname = entryList["FirstName"]
    lname = entryList["LastName"]
    del entryList["FirstName"]
    del entryList["LastName"]
    for k, v in entryList.items():
        entryList[k] = v.get()

    newList = {name : entryList}
    saveToFile(newList)
    rootWindow.destroy()

def employeeInfoWdw(root,name,guiInstance):
    #Get the button that stores this individual employee's name
    buttonInstance = guiInstance.buttonList[name]

    #Window specs
    new_window = tb.Toplevel(root)
    new_window.title(name + "'s info")
    new_window.geometry("600x500")
    new_window.resizable(False, False)

    #Title
    label = tb.Label(new_window, text=name + "'s info, override if necessary ", font=("Helvetica", 13)).pack(pady=5)

    #Save Button
    close_button = tb.Button(new_window, text="Save/Close", command=lambda: save(new_window, entryList,name),
                             bootstyle="success,outline")
    close_button.pack(side="bottom")

    #Delete Button
    delete_button = tb.Button(new_window, text="DELETE",bootstyle="danger,outline")
    delete_button.place(relx=0, rely=1, anchor="sw")

    #Stores employee info
    entryList = {}

    #Check if list exist, it should be impossible for it to not exist if execution reaches here
    LIST = getEmployeeList()
    if LIST is None or name not in LIST:
        raise Exception("Error, Invalid Employee List or Employee does not Exist!")
    values = LIST[name]

    #Frames to hold widgets
    details_frame = tb.Frame(new_window, width=0)
    details_frame.pack(side="left", anchor="n", pady=15, padx=10)

    details_frame2 = tb.Frame(new_window, width=200)
    details_frame2.pack(side="right", anchor="n", pady=15, padx=10, expand=True, fill="x")

    #Personal information Label
    tb.Label(details_frame, text="Personal Information", bootstyle="success", font=("Helvetica", 11)).grid(row=0,
                                                                                                           column=0,
                                                                                                           pady=10)

    # Create labels and entry widgets for employee first Name
    tb.Label(details_frame, text="Employee First Name:").grid(row=1, column=0, sticky="e", pady=(0, 5))
    name_entry = tb.Label(details_frame, width=15, text=name.split()[0])
    name_entry.grid(row=1, column=1, sticky="w", pady=(0, 5))
    entryList["FirstName"] = name.split()[0]

    # Create labels and entry widgets for employee last Name
    tb.Label(details_frame, text="Employee Last Name:").grid(row=2, column=0, sticky="e", pady=(0, 5))
    last_name_entry = tb.Label(details_frame, width=15, text=name.split()[1])
    last_name_entry.grid(row=2, column=1, sticky="w", pady=(0, 5))
    entryList["LastName"] = name.split()[1]

    # Create labels and entry widgets for employee DOB
    tb.Label(details_frame, text="Employee Date of Birth:").grid(row=3, column=0, sticky="e", pady=(0, 5))
    dob_entry = tb.Entry(details_frame, width=15)
    dob_entry.insert(0, values["Date Of Birth"])
    dob_entry.grid(row=3, column=1, sticky="w", pady=(0, 5))
    entryList["Date Of Birth"] = dob_entry

    # Create labels and entry widgets for employee Sex
    tb.Label(details_frame, text="Employee Sex:").grid(row=4, column=0, sticky="e", pady=(0, 5))
    gender_entry = tb.Entry(details_frame, width=15)
    gender_entry.insert(0, values["Sex"])
    gender_entry.grid(row=4, column=1, sticky="w", pady=(0, 5))
    entryList["Sex"] = gender_entry

    # Create labels and entry widgets for employee Race
    tb.Label(details_frame, text="Employee Race:").grid(row=5, column=0, sticky="e", pady=(0, 5))
    race_entry = tb.Entry(details_frame, width=15)
    race_entry.insert(0, values["Race"])
    race_entry.grid(row=5, column=1, sticky="w", pady=(0, 5))
    entryList["Race"] = race_entry

    #Contact Information Label
    tb.Label(details_frame, text="Contact Information", bootstyle="success", font=("Helvetica", 11)).grid(row=6,
                                                                                                          column=0,
                                                                                                          sticky="e",
                                                                                                          pady=22)
    # Create labels and entry widgets for employee Email
    tb.Label(details_frame, text="Employee Email:").grid(row=7, column=0, sticky="e", pady=(0, 5))
    email_entry = tb.Entry(details_frame, width=17)
    email_entry.insert(0, values["Email"])
    email_entry.grid(row=7, column=1, sticky="w", pady=(0, 5))
    entryList["Email"] = email_entry

    # Create labels and entry widgets for employee Phone
    tb.Label(details_frame, text="Employee Phone:").grid(row=8, column=0, sticky="e", pady=(0, 5))
    phone_entry = tb.Entry(details_frame, width=17)
    phone_entry.insert(0, values["Phone"])
    phone_entry.grid(row=8, column=1, sticky="w", pady=(0, 5))
    entryList["Phone"] = phone_entry

    # Create labels and entry widgets for employee Address
    tb.Label(details_frame, text="Employee Address:").grid(row=9, column=0, sticky="e", pady=(0, 5))
    address_entry = tb.Entry(details_frame, width=17)
    address_entry.insert(0, values["Address"])
    address_entry.grid(row=9, column=1, sticky="w", pady=(0, 5))
    entryList["Address"] = address_entry

    # Create labels and entry widgets for employee ID
    tb.Label(details_frame, text="Employee ID:").grid(row=10, column=0, sticky="e", pady=(0, 5))
    ID_entry = tb.Entry(details_frame, width=17)
    ID_entry.insert(0, values["Employee ID"])
    ID_entry.grid(row=10, column=1, sticky="w", pady=(0, 5))
    entryList["Employee ID"] = ID_entry

    #Employment Details Label
    tb.Label(details_frame2, text="Employment Details", bootstyle="success", font=("Helvetica", 11)).grid(row=0,
                                                                                                          column=3,
                                                                                                          pady=10)
    # Create labels and entry widgets for employee Job Title
    tb.Label(details_frame2, text="Job Title:").grid(row=1, column=3, pady=(0, 5), sticky="e")
    job_entry = tb.Entry(details_frame2, width=15)
    job_entry.insert(0, values["Job Title"])
    job_entry.grid(row=1, column=4, sticky="w", pady=(0, 5))
    entryList["Job Title"] = job_entry

    # Create labels and entry widgets for employee Job Department
    tb.Label(details_frame2, text="Department:").grid(row=2, column=3, pady=(0, 5), sticky="e")
    department_entry = tb.Entry(details_frame2, width=15)
    department_entry.insert(0, values["Department"])
    department_entry.grid(row=2, column=4, sticky="w", pady=(0, 5))
    entryList["Department"] = department_entry

    # Create labels and entry widgets for employee Superior
    tb.Label(details_frame2, text="Manager/Leader:").grid(row=3, column=3, pady=(0, 5), sticky="e")
    manager_entry = tb.Entry(details_frame2, width=15)
    manager_entry.insert(0, values["Manager/Leader"])
    manager_entry.grid(row=3, column=4, sticky="w", pady=(0, 5))
    entryList["Manager/Leader"] = manager_entry

    # Create labels and entry widgets for employee Job Status
    tb.Label(details_frame2, text="Employment Status:").grid(row=4, column=3, pady=(0, 5), sticky="e")
    status_entry = tb.Entry(details_frame2, width=15)
    status_entry.insert(0, values["Status"])
    status_entry.grid(row=4, column=4, sticky="w", pady=(0, 5))
    entryList["Status"] = status_entry

    # Create labels and entry widgets for employee Salary
    tb.Label(details_frame2, text="Salary:").grid(row=5, column=3, pady=(0, 5), sticky="e")
    salary_entry = tb.Entry(details_frame2, width=15)
    salary_entry.insert(0, values["Salary"])
    salary_entry.grid(row=5, column=4, sticky="w", pady=(0, 5))
    entryList["Salary"] = salary_entry

    #Performance & Development Label
    tb.Label(details_frame2, text="Performance & Development", bootstyle="success", font=("Helvetica", 11)).grid(row=6,
                                                                                                                 column=3,
                                                                                                                 columnspan=2,
                                                                                                                 pady=10)
    # Create labels and entry widgets for employee Attendance
    tb.Label(details_frame2, text="Time and Attendance:").grid(row=7, column=3, pady=(0, 5), sticky="e")
    time_entry = tb.Entry(details_frame2, width=15)
    time_entry.insert(0, values["Time and Attendance"])
    time_entry.grid(row=7, column=4, sticky="w", pady=(0, 5))
    entryList["Time and Attendance"] = time_entry

    # Create labels and entry widgets for employee Skills
    tb.Label(details_frame2, text="Certifications and Skills:").grid(row=8, column=3, pady=(0, 5), sticky="e")
    certs_entry = tb.Entry(details_frame2, width=15)
    certs_entry.insert(0, values["Certifications and Skills"])
    certs_entry.grid(row=8, column=4, sticky="w", pady=(0, 5))
    entryList["Certifications and Skills"] = certs_entry

    # Create labels and entry widgets for employee Programs
    tb.Label(details_frame2, text="Training/Programs:").grid(row=9, column=3, pady=(0, 5), sticky="e")
    training = tb.Entry(details_frame2, width=15)
    training.insert(0, values["Training/Programs"])
    training.grid(row=9, column=4, sticky="w", pady=(0, 5))
    entryList["Training/Programs"] = training

    # Create labels and entry widgets for employee extra Info
    tb.Label(details_frame2, text="Any Extra Information:").grid(row=10, column=3, pady=(0, 5), sticky="e")
    extra_entry = tb.Entry(details_frame2, width=15)
    extra_entry.insert(0, values["Extra Information"])
    extra_entry.grid(row=10, column=4, sticky="w", pady=(0, 5))
    entryList["Extra Information"] = extra_entry