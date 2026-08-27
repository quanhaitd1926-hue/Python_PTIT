from math import *
from collections import *
from datetime import *

class TimeCalculation:
    def __init__(self, id, name, startTime, endTime):
        self.id = id
        self.name = name
        self.startTime = startTime
        self.endTime = endTime
        self.totalTime = self.calculatorTotalTime()

    def calculatorTotalTime(self):
        startTime = datetime.strptime(self.startTime, "%H:%M")
        endTime = datetime.strptime(self.endTime, "%H:%M")
        total = endTime - startTime
        return total.seconds // 60
        

    def toString(self):
        hours = self.totalTime // 60
        minutes = self.totalTime % 60
        return "{} {} {} gio {} phut".format(self.id, self.name, hours, minutes)

if __name__ == "__main__":
    n = int(input())
    listTime = []
    for i in range(n):
        id = input()
        name = input()
        startTime = input()
        endTime = input()
        listTime.append(TimeCalculation(id, name, startTime, endTime))

    listTime.sort(key=lambda time: time.totalTime, reverse=True)

    for timeCalculation in listTime:
        print(timeCalculation.toString())
        