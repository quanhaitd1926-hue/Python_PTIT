class Teacher:
    def __init__(self, id, name, admissionCode):
        self.id = "GV" + f"{id:02d}"
        self.name = name
        self.subject = getSubject(admissionCode)
        self.score = 0.0
        self.result = ""

    def toString(self):
        return self.id + " " + self.name + " " + self.subject + " " + f"{self.score:.1f}" + " " + self.result

def getSubject(admissionCode):
    if admissionCode[0] == "A":
        return "TOAN"
    elif admissionCode[0] == "B":
        return "LY"
    else:
        return "HOA"

def calculatorTotalScore(admissionCode, s1, s2):
    if admissionCode[1] == "1": return s1 * 2 + s2 + 2.0
    elif admissionCode[1] == "2": return s1 * 2 + s2 + 1.5
    elif admissionCode[1] == "3": return s1 * 2 + s2 + 1.0
    else: return s1 * 2 + s2


def status(score):
    if score >= 18:
        return "TRUNG TUYEN"
    else:
        return "LOAI"


if __name__ == "__main__":
    n = int(input())
    listTeacher = []

    for i in range(n):
        name = input()
        admissionCode = input()
        s1 = float(input())
        s2 = float(input())

        teacher = Teacher(i + 1, name, admissionCode)
        teacher.score = calculatorTotalScore(admissionCode, s1, s2)
        teacher.result = status(teacher.score)

        listTeacher.append(teacher)

    listTeacher.sort(key=lambda teacher: (-teacher.score, teacher.id))

    for teacher in listTeacher:
        print(teacher.toString())