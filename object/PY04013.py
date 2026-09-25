from datetime import datetime

class Rain:
    def __init__(self, address, startTime, endTime, rain):
        self.address = address
        self.startTime = startTime
        self.endTime = endTime
        self.rain = rain

def handleCreateId(cnt):
    return "T" + f"{cnt:02d}"

def solve(startTime, endTime):
    stTime = datetime.strptime(startTime, "%H:%M")
    eTime = datetime.strptime(endTime, "%H:%M")
    return (eTime - stTime).seconds / 60

if __name__ == "__main__":
    n = int(input())
    cnt = [0] * (n + 5)
    listRain = []
    for i in range(n):
        address = input().strip()
        startTime = input().strip()
        endTime = input().strip()
        rain = int(input().strip())
        listRain.append(Rain(address, startTime, endTime, rain))

    count = 1
    for i in range(n):
        totalTime = 0
        totalRain = 0
        if cnt[i] == 0:
            cnt[i] = 1
            totalTime += solve(listRain[i].startTime, listRain[i].endTime)
            totalRain += listRain[i].rain
            for j in range(i + 1, n):
                if listRain[i].address == listRain[j].address:
                    totalTime += solve(listRain[j].startTime, listRain[j].endTime)
                    totalRain += listRain[j].rain
                    cnt[j] = 1
            print(handleCreateId(count) + " " + listRain[i].address, end=" ")
            print(f"{(1.0 * totalRain / totalTime) * 60:.2f}")
            count += 1
    