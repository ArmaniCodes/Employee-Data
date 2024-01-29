from modules import *




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