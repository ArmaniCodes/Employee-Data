from Modules import *
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg


class graphGUI():
    def __init__(self,root):
        self.root = root
        self.createGraphFrame(self.root)

    def createGraphFrame(self, root):
        self.graphFrame = tb.Frame(root, style="My.TFrame", width=750, height=430)
        self.graphFrame.place(x=380, y=20)


    def createGraphs(self,employeeStatsRef,employees):
        pass