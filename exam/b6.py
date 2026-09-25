from datetime import datetime

class Subject:
    def __init__(self, id, idSubject, name, dayOfDate, time, examGroup):
        self.id = f'T{str(id).zfill(3)}'
        self.idSubject = idSubject
        self.name = name
        self.dayOfDate = dayOfDate
        self.dayOfDateSort = datetime.strptime(dayOfDate, '%d/%m/%Y')
        self.time = time
        self.timeSort = datetime.strptime(time, '%H:%M')
        self.examGroup = examGroup

    def toString(self):
        return str.format("{} {} {} {} {} {}", self.id, self.idSubject, self.name, self.dayOfDate, self.time, self.examGroup)

if __name__ == "__main__":
    n, m = map(int, input().split())
    dic = {}
    for _ in range(n):
        idSubject = input()
        name = input()
        dic[idSubject] = name
    listSubject = []
    for i in range(m):
        idSubject, dayOfDate, time, examGroup = map(str, input().split())
        listSubject.append(Subject(i + 1, idSubject, dic[idSubject], dayOfDate, time, examGroup))

    listSubject.sort(key=lambda subject: (subject.dayOfDateSort, subject.timeSort, subject.id))

    for subject in listSubject:
        print(subject.toString())

    