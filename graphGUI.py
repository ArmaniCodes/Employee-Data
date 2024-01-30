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
        self.create_gender_piechart([employeeStatsRef.maleCount, employeeStatsRef.femaleCount], ['M','F'])
        self.create_donut_chart(employeeStatsRef)

    #Employment Status Breakdown Chart
    def create_donut_chart(self,employeeStatsRef):
        chart_frame = tk.Frame(self.root, width=0, height=0)
        chart_frame.place(x=395, y=250)
        #Total of status stats
        total = sum(employeeStatsRef.employmentType.values())

        #Format values
        values = list(
            ({category: (value / total) * 100 for category, value in employeeStatsRef.employmentType.items()}).values())
        labels = employeeStatsRef.employmentType.keys()

        #Graph theme
        colors = ['lightblue', 'lightcoral', 'pink', 'red']
        textprops = {'fontsize': 7, 'color': 'white', 'weight': 'bold'}

        #Graph creation
        fig, ax = plt.subplots()
        ax.set_title('Employment Status Breakdown', fontdict={'color': 'white', 'size': 9})
        ax.pie(values, labels=labels, autopct='%1.1f%%', startangle=90, wedgeprops=dict(width=0.4, edgecolor='black'),
               textprops=textprops, labeldistance=0.9)

        #Set canvas to transparent
        fig.patch.set_alpha(0.0)
        ax.set_facecolor((0, 0, 0, 0.0))
        ax.axis('equal')

        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.configure(width=200, height=190, bg='gray20')
        canvas_widget.pack()


    def formatLineChartData(self,employees):
        bin_size = 5
        min_age = min(employee["Age"] for employee in employees.values())
        max_age = max(employee["Age"] for employee in employees.values())
        bins = [i for i in range(min_age, max_age + bin_size, bin_size)]

        # Initialize age_salaries dictionary
        age_salaries = {bin_center: [] for bin_center in range(min_age + bin_size // 2, max_age, bin_size)}

        # Fill age_salaries dictionary with corresponding salary data
        for employee in employees.values():
            for bin_center in age_salaries.keys():
                bin_start = bin_center - bin_size // 2
                bin_end = bin_center + bin_size // 2
                if bin_start <= employee["Age"] < bin_end:
                    age_salaries[bin_center].append(int(employee["Salary"]))

    def create_lineChart(self, employees):
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
        canvas = FigureCanvasTkAgg(fig, master=chart_frame)
        canvas_widget = canvas.get_tk_widget()
        canvas_widget.configure(width=200, height=200, background="gray20")
        canvas_widget.pack()