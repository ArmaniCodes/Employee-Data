from modules import *




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