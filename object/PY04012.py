class CaculatorScore:

    score = 0

    def __init__(self, id, name, className):
            self.id = id
            self.name = name
            self.className = className

    def toString(self):
        return self.id + " " + self.name + " " + self.className + " " + str(self.score)

if __name__ == "__main__":
    n = int(input())
    arrList = []
    for i in range(n):
        id = input()
        name = input()
        className = input()
        arrList.append(CaculatorScore(id, name, className))
    for i in range(n):
        id, attendance = map(str, input().split())
        for j in range(len(arrList)):
            if id == arrList[j].id:
                score = 10
                for k in range(len(attendance)):
                    if attendance[k] == "m": score -= 1
                    elif attendance[k] == "v": score -= 2
                    else: continue
                if score <= 0: arrList[j].score = 0
                else: arrList[j].score = score
                break
    for i in range(len(arrList)):
        print(arrList[i].toString(), end="")
        if arrList[i].score == 0: print(" KDDK")
        else: print()

