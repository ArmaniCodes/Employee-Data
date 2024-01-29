from Modules import *
from manageFile import getEmployeeList
from newEmployeeGUI import newEmployeeWdw
class EmployeeGui:
    def __init__(self):
        #Dark Theme
        self.root = tb.Window(themename="darkly")
        #Window Size
        self.root.geometry("1150x500")
        self.root.resizable(False, False)
        self.root.title("Employee Dashboard")

        self.employeeCount = 0
        self.buttonList = {}

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
                           command=lambda: newEmployeeWdw(self.root, self.instance)         )
        button.pack(side="bottom", anchor="w")

        #Employee Count Label
        self.empCountLabel = tb.Label(self.root, text="Employees: 0", bootstyle="success", width=17)
        self.empCountLabel.pack(side="bottom", anchor="w")

        #Canvas for scroll bar
        self.canvas = tb.Canvas(frame, yscrollcommand=scrollbar.set, width=150, height=300)
        self.canvas.pack(side="left", fill="y")
        scrollbar.configure(command=self.canvas.yview)
        self.createEmployeeFrame()

    def createEmployeeFrame(self):
        self.inner_frame = tk.Frame(self.canvas)
        #Creates window
        self.canvas.create_window((0, 0), window=self.inner_frame, anchor="nw")
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    #Adds new employee to Frame and updates scrollingFrame
    def addEmployeeToFrame(self,name):
        pass

    def clearEmployees(self):
        #Destroying this clears all it's children AKA employees
        self.inner_frame.destroy()
        #Create new frame with no employees
        self.createEmployeeFrame()


    #Updates frame when new employees Loaded/Deleted
    def updateScrollingFrame(self):
        self.inner_frame.update_idletasks()
        self.canvas.config(scrollregion=self.canvas.bbox("all"))

    def updateEmployeeLabel(self,employeeCount):
        self.empCountLabel.configure(text = "Employees: " + str(employeeCount))

    def LoadEmployees(self):
        employees = getEmployeeList()
        if employees:
            self.clearEmployees() #Clear Previous Employees

            #Button Style that gives transparent appearance
            stylex = tb.Style()
            background_color = self.root.cget("background")
            stylex.configure("Custom.TButton", background=background_color, bordercolor=background_color,
                             lightcolor=background_color, darkcolor=background_color, highlightthickness=0, bd=0)
            #Set Employee Count to 0 before counting
            self.employeeCount = 0

            for i in employees:
                self.employeeCount+=1
                b = tb.Button(self.inner_frame, width=20, text=i, style="Custom.TButton")

                self.buttonList[i] = b
                b.pack(fill="x")
            self.updateScrollingFrame()
            self.updateEmployeeLabel()
        else:
            self.clearEmployees()