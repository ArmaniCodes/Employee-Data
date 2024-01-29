from Modules import *


class EmployeeGui:
    def __init__(self):
        #Dark Theme
        self.root = tb.Window(themename="darkly")
        #Window Size
        self.root.geometry("1150x500")
        self.root.resizable(False, False)
        self.root.title("Employee Dashboard")

        #Store instance of GUI for later Use
        self.instance = self
        self.createGui()
        self.root.mainloop()

    def createGui(self):
        frame = tb.Frame(self.root)

        frame.pack(side="left",fill = "y")
        scrollbar = tb.Scrollbar(frame, orient="vertical")
        scrollbar.pack(side="right", fill="y")

        #Setup buttons
        button = tb.Button(self.root, text="LOAD EMPLOYEES", command=self.LoadEmployees, bootstyle="light-outline",
                           width=17)
        button.pack(side="bottom", anchor="w")
        button = tb.Button(self.root, width=17, bootstyle="light-outline", text="NEW EMPLOYEE",
                           command=lambda: newEmployeeWdw(self.root, self.instance))
        button.pack(side="bottom", anchor="w")

        #Employee Count Label
        self.empCountLabel = tb.Label(self.root, text="Employees: 0", bootstyle="success", width=17)
        self.empCountLabel.pack(side="bottom", anchor="w")