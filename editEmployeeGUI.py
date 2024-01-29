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