import math

class Triangle:
    def __init__(self, e1, e2, e3):
        self.e1 = e1
        self.e2 = e2
        self.e3 = e3

    def perimeterTriangle(self):
        res = self.e1 + self.e2 + self.e3
        return f"{res:.3f}"

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        x1, y1, x2, y2, x3, y3 = map(float, input().split())
        e1 = math.sqrt(math.pow(x2 - x1, 2) + math.pow(y2 - y1, 2))
        e2 = math.sqrt(math.pow(x2 - x3, 2) + math.pow(y2 - y3, 2))
        e3 = math.sqrt(math.pow(x3 - x1, 2) + math.pow(y3 - y1, 2))
        if e1 + e2 <= e3 or e2 + e3 <= e1 or e1 + e3 <= e2: print("INVALID")
        else:
            triangle = Triangle(e1, e2, e3)
            print(triangle.perimeterTriangle())