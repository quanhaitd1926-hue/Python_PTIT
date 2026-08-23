import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, p):
        dis = math.sqrt(math.pow(p.x - self.x, 2) + math.pow(p.y - self.y, 2))
        return f"{dis:.4f}" 

def Decimal(s):
    return float(s)


if __name__ == '__main__':
    t = int(input())
    while t > 0:
        arr = input().split()
        p1 = Point(Decimal(arr[0]), Decimal(arr[1]))
        p2 = Point(Decimal(arr[2]), Decimal(arr[3]))
        print(p1.distance(p2))
        t -= 1