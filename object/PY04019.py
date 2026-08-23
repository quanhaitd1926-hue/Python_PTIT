class Employee:
    def __init__(self, id, name):
        self.id = "TS0" + str(id)
        self.name = name
        self.score = 0.0
        self.status = ""

    def toString(self):
        return self.id + " " + self.name + " " + f"{self.score:.2f}" + " " + self.status

def calculatorScore(theoryScore, practiceScore):
    return (theoryScore + practiceScore) / 2.0

def getStatus(score):
    if score < 5: return "TRUOT"
    elif score < 8: return "CAN NHAC"
    elif score <= 9.5: return "DAT"
    else: return "XUAT SAC"

if __name__ == "__main__":
    n = int(input())
    listEmployee = []
    for i in range(n):
        name = input()
        theoryScore = float(input())
        practiceScore = float(input())
        if theoryScore > 10: theoryScore /= 10.0
        if practiceScore > 10: practiceScore /= 10.0
        employee = Employee(i + 1, name)
        employee.score = calculatorScore(theoryScore, practiceScore)
        employee.status = getStatus(employee.score)
        listEmployee.append(employee)
    listEmployee.sort(key=lambda employee: -employee.score) 
    for employee in listEmployee:
        print(employee.toString())
