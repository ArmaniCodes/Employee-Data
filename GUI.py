from modules import *


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


    def createGui(self):
        frame = tb.Frame(self.root)