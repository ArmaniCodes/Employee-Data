from modules import *
from manageFile import getEmployeeList



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
    close_button = tb.Button(new_window, text="Save/Close", command=lambda: save(new_window, entryList),
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