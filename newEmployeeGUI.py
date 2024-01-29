from Modules import *




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