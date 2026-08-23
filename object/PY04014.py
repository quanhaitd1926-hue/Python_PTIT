class Score:
    def __init__(self, id, name, gpa):
        self.id = "HS" + f"{id:02d}"
        self.name = name
        self.gpa = gpa

    def toString(self):
        return self.id + " " + self.name + " " + f"{self.gpa:.1f}"

if __name__ == "__main__":
    n = int(input())
    arrList = []
    for i in range(1, n + 1):
        name = input()
        res = list(map(float, input().split()))
        result = 0.0
        for j in range(len(res)):
            if j == 0 or j == 1:
                result += res[j] * 2
            else: result += res[j]
        gpa = int(result / 12 * 10 + 0.5) / 10.0
        arrList.append(Score(i, name, gpa))
    sorted_arrList = sorted(arrList, key=lambda score: (-score.gpa, score.id))
    for i in range(n):
        print(sorted_arrList[i].toString(), end=" ")
        if sorted_arrList[i].gpa >= 9: print("XUAT SAC")
        elif sorted_arrList[i].gpa >= 8: print("GIOI")
        elif sorted_arrList[i].gpa >= 7: print("KHA")
        elif sorted_arrList[i].gpa >= 5: print("TB")
        else: print("YEU")
