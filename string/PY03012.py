class Student:
    def __init__(self, name, totalAssignmentCorrect, totalSubmit):
        self.name = name
        self.totalAssignmentCorrect = totalAssignmentCorrect
        self.totalSubmit = totalSubmit

    def toString(self):
        return "{} {} {}".format(self.name, self.totalAssignmentCorrect, self.totalSubmit)

if __name__ == "__main__":
    n = int(input())
    listStudents = []
    for i in range(n):
        name = input()
        totalAssignmentCorrect, totalSubmit = map(int, input().split())
        listStudents.append(Student(name, totalAssignmentCorrect, totalSubmit))
    listStudents.sort(key=lambda student: (-student.totalAssignmentCorrect, student.totalSubmit, student.name))
    for student in listStudents:
        print(student.toString())