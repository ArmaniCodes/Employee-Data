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


    #Sex Distribution Pie chart
    def create_gender_piechart(self,data,labels):
        fig, ax = plt.subplots()
        fig.patch.set_alpha(0)
        ax.set_title('Sex Distribution', fontdict={'color': 'white', 'size': 9})

        colors = ['#26358a', '#00E2A9']
        ax.pie(data, labels=labels, autopct='%1.1f%%', startangle=50, textprops={'fontsize': 8, 'color': 'white'},
               colors=colors, wedgeprops=dict(width=0.4, edgecolor='black'))
        ax.axis('equal')

        chart_frame = tk.Frame(self.root, width=0, height=0)
        chart_frame.place(x=395, y=25)