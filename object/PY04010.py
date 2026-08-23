class Student:
    def __init__(self, name, birth, p1, p2, p3):
        self.name = name
        self.birth = birth
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3

    def sumPoint(self):
        res = self.p1 + self.p2 + self.p3
        return f"{res:.1f}"

    def toString(self):
        return self.name + " " + self.birth + " " + self.sumPoint()

if __name__ == "__main__":
    name = input()
    birth = input()
    p1 = float(input())
    p2 = float(input())
    p3 = float(input())
    student = Student(name, birth, p1, p2, p3)
    print(student.toString())
