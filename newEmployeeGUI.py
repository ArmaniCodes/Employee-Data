from Modules import *


#Save Data
def save(new_window,entryList,guiInstance):
    #Convert entry to the entries text from v.get()
    for k,v in entryList.items():
        list[k] = v.get()

    fname = list["FirstName"]
    lname = list["LastName"]
    del list["FirstName"]
    del list["LastName"]

#Create New EmployeeGUI
def newEmployeeWdw(root,guiInstance):
    #Window specs
    new_window = tb.Toplevel(root)
    new_window.title("Employee Information")
    new_window.geometry("600x500")
    new_window.resizable(False, False)

    #Title
    label = tb.Label(new_window, text="Enter your employees info", font=("Helvetica", 13)).pack(pady=5)

    #Save Button
    close_button = tb.Button(new_window, text="Save", command=lambda: save(new_window, entryList, guiInstance),
                             bootstyle="success,outline")
    close_button.pack(side="bottom")

    #Store Entries in form of dictionary
    entryList = {}

    #Frames to store labels/Entries
    details_frame = tb.Frame(new_window, width=0)
    details_frame.pack(side="left", anchor="n", pady=15, padx=10)

    details_frame2 = tb.Frame(new_window, width=200)
    details_frame2.pack(side="right", anchor="n", pady=15, padx=10, expand=True, fill="x")

    #Personal Information Label
    tb.Label(details_frame, text="Personal Information", bootstyle="success", font=("Helvetica", 11)).grid(row=0,
                                                                                                           column=0,
                                                                                                           pady=10)
    # Create label and entry widget for employee first Name, then store in entryList
    tb.Label(details_frame, text="Employee First Name:").grid(row=1, column=0, sticky="e", pady=(0, 5))
    name_entry = tb.Entry(details_frame, width=15)
    name_entry.grid(row=1, column=1, sticky="w", pady=(0, 5))
    entryList["FirstName"] = name_entry

    # Create label and entry widget for employee Last Name, then store in entryList
    tb.Label(details_frame, text="Employee Last Name:").grid(row=2, column=0, sticky="e", pady=(0, 5))
    last_name_entry = tb.Entry(details_frame, width=15)
    last_name_entry.grid(row=2, column=1, sticky="w", pady=(0, 5))
    entryList["LastName"] = last_name_entry

    # Create label and entry widget for employee DOB, then store in entryList
    tb.Label(details_frame, text="Employee Date of Birth:").grid(row=3, column=0, sticky="e", pady=(0, 5))
    dob_entry = tb.Entry(details_frame, width=15)
    dob_entry.grid(row=3, column=1, sticky="w", pady=(0, 5))
    entryList["Date Of Birth"] = dob_entry

    # Create label and entry widget for employee sex, then store in entryList
    tb.Label(details_frame, text="Employee Sex:").grid(row=4, column=0, sticky="e", pady=(0, 5))
    sex_entry = tb.Entry(details_frame, width=15)
    sex_entry.grid(row=4, column=1, sticky="w", pady=(0, 5))
    entryList["Sex"] = sex_entry

    # Create label and entry widget for employee race, then store in entryList
    tb.Label(details_frame, text="Employee Race:").grid(row=5, column=0, sticky="e", pady=(0, 5))
    race_entry = tb.Entry(details_frame, width=15)
    race_entry.grid(row=5, column=1, sticky="w", pady=(0, 5))
    entryList["Race"] = race_entry

    #Contact Information Label
    tb.Label(details_frame, text="Contact Information", bootstyle="success", font=("Helvetica", 11)).grid(row=6,
                                                                                                          column=0,
                                                                                                          sticky="e",
                                                                                                          pady=10)
    # Create label and entry widget for employee's email, then store in entryList
    tb.Label(details_frame, text="Employee Email:").grid(row=7, column=0, sticky="e", pady=(0, 5))
    email_entry = tb.Entry(details_frame, width=17)
    email_entry.grid(row=7, column=1, sticky="w", pady=(0, 5))
    entryList["Email"] = email_entry

    # Create label and entry widget for employee's phone, then store in entryList
    tb.Label(details_frame, text="Employee Phone:").grid(row=8, column=0, sticky="e", pady=(0, 5))
    phone_entry = tb.Entry(details_frame, width=17)
    phone_entry.grid(row=8, column=1, sticky="w", pady=(0, 5))
    entryList["Phone"] = phone_entry

    # Create label and entry widget for employee's address, then store in entryList
    tb.Label(details_frame, text="Employee Address:").grid(row=9, column=0, sticky="e", pady=(0, 5))
    address_entry = tb.Entry(details_frame, width=17)
    address_entry.grid(row=9, column=1, sticky="w", pady=(0, 5))
    entryList["Address"] = address_entry

    # Create label and entry widget for employee's ID, then store in entryList
    tb.Label(details_frame, text="Employee ID:").grid(row=10, column=0, sticky="e", pady=(0, 5))
    ID_entry = tb.Entry(details_frame, width=17)
    ID_entry.grid(row=10, column=1, sticky="w", pady=(0, 5))
    entryList["Employee ID"] = ID_entry

    #Employment Details Label
    tb.Label(details_frame2, text="Employment Details", bootstyle="success", font=("Helvetica", 11)).grid(row=0,
                                                                                                          column=3,
                                                                                                          pady=10)
    # Create label and entry widget for employee's Job Title, then store in entryList
    tb.Label(details_frame2, text="Job Title:").grid(row=1, column=3, pady=(0, 5), sticky="e")
    job_entry = tb.Entry(details_frame2, width=15)
    job_entry.grid(row=1, column=4, sticky="w", pady=(0, 5))
    entryList["Job Title"] = job_entry

    # Create label and entry widget for employee's department, then store in entryList
    tb.Label(details_frame2, text="Department:").grid(row=2, column=3, pady=(0, 5), sticky="e")
    department_entry = tb.Entry(details_frame2, width=15)
    department_entry.grid(row=2, column=4, sticky="w", pady=(0, 5))
    entryList["Department"] = department_entry

    # Create label and entry widget for employee's Manager/Leader, then store in entryList
    tb.Label(details_frame2, text="Manager/Leader:").grid(row=3, column=3, pady=(0, 5), sticky="e")
    manager_entry = tb.Entry(details_frame2, width=15)
    manager_entry.grid(row=3, column=4, sticky="w", pady=(0, 5))
    entryList["Manager/Leader"] = manager_entry

    # Create label and entry widget for employees employment status, then store in entryList
    tb.Label(details_frame2, text="Employment Status:").grid(row=4, column=3, pady=(0, 5), sticky="e")
    status_entry = tb.Entry(details_frame2, width=15)
    status_entry.grid(row=4, column=4, sticky="w", pady=(0, 5))
    entryList["Status"] = status_entry

    # Create label and entry widget for employees salary, then store in entryList
    tb.Label(details_frame2, text="Salary:").grid(row=5, column=3, pady=(0, 5), sticky="e")
    salary_entry = tb.Entry(details_frame2, width=15)
    salary_entry.grid(row=5, column=4, sticky="w", pady=(0, 5))
    entryList["Salary"] = salary_entry

    #Performance Label
    tb.Label(details_frame2, text="Performance & Development", bootstyle="success", font=("Helvetica", 11)).grid(row=6,
                                                                                                                 column=3,
                                                                                                                 columnspan=2,
                                                                                                                 pady=10)
    # Create label and entry widget for employees attendance, then store in entryList
    tb.Label(details_frame2, text="Time and Attendance:").grid(row=7, column=3, pady=(0, 5), sticky="e")
    time_entry = tb.Entry(details_frame2, width=15)
    time_entry.grid(row=7, column=4, sticky="w", pady=(0, 5))
    entryList["Time and Attendance"] = time_entry

    # Create label and entry widget for employees skills, then store in entryList
    tb.Label(details_frame2, text="Certifications and Skills:").grid(row=8, column=3, pady=(0, 5), sticky="e")
    certs_entry = tb.Entry(details_frame2, width=15)
    certs_entry.grid(row=8, column=4, sticky="w", pady=(0, 5))
    entryList["Certifications and Skills"] = certs_entry

    # Create label and entry widget for employees training, then store in entryList
    tb.Label(details_frame2, text="Training/Programs:").grid(row=9, column=3, pady=(0, 5), sticky="e")
    training = tb.Entry(details_frame2, width=15)
    training.grid(row=9, column=4, sticky="w", pady=(0, 5))
    entryList["Training/Programs"] = training

    # Create label and entry widget for employees extra Info, then store in entryList
    tb.Label(details_frame2, text="Any Extra Information:").grid(row=10, column=3, pady=(0, 5), sticky="e")
    extra_entry = tb.Entry(details_frame2, width=15)
    extra_entry.grid(row=10, column=4, sticky="w", pady=(0, 5))
    entryList["Extra Information"] = extra_entry