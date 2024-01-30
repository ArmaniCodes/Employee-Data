class EmployeeStatistics():
    def __init__(self):
        self.employeeCount = 0
        self.maleCount = 0
        self.femaleCount = 0
        self.employmentType = {"Full Time": 0, "Part Time": 0, "Internship": 0, "Contract": 0}


    def increaseMaleCount(self):
        self.maleCount+=1
    def increaseFemaleCount(self):
        self.femaleCount+=1
    def decreaseMaleCount(self):
        self.maleCount-=1
    def decreaseFemaleCount(self):
        self.femaleCount-=1

    def sortStats(self,employeeData):
        if employeeData["Sex"] == "Male":
            self.increaseMaleCount()
        if employeeData["Sex"] == "Female":
            self.increaseFemaleCount()

        self.employmentType[employeeData["Status"]] += 1