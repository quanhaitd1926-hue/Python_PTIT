from datetime import datetime

class Player:
    def __init__(self, name, address, endTime):
        self.name = name
        self.address = address
        self.endTime = endTime
        self.id = self.createId()
        self.velocity = self.calculateVelocity()

    def createId(self):
        id = ""
        add = self.address.split()
        for i in range(len(add)):
            id += add[i][0]
        name = self.name.split()
        for i in range(len(name)):
            id += name[i][0]
        return id

    def calculateVelocity(self):
        startTime = datetime.strptime("6:00", "%H:%M")
        endTime = datetime.strptime(self.endTime, "%H:%M")
        totalTime = (endTime - startTime).total_seconds() / 3600
        return 120 / totalTime


    def toString(self):
        return "{} {} {} {:.0f} Km/h".format(self.id, self.name, self.address, self.velocity)

if __name__ == "__main__":
    n = int(input())
    listPlayer = []
    for i in range(n):
        name = input().strip()
        address = input().strip()
        endTime = input().strip()
        listPlayer.append(Player(name, address, endTime))

    listPlayer.sort(key=lambda player: player.velocity, reverse=True)

    for player in listPlayer:
        print(player.toString())
