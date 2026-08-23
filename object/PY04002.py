class Rectangle:
    def __init__(self, length: int, width: int, colorr: str):
        if length <= 0 or width <= 0:
            print("INVALID")
            raise SystemExit
        
        self.length = length
        self.width = width
        self.colorr = colorr

    def perimeter(self):
        return 2 * (self.length + self.width)

    def area(self):
        return self.length * self.width

    def color(self):
        return self.colorr.capitalize()

if __name__ == '__main__':
    arr = input().split()
    r = Rectangle(int(arr[0]), int(arr[1]), str(arr[2]))
    print('{} {} {}'.format(r.perimeter(), r.area(), r.color()))
