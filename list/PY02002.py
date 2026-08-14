f = [0] * 100
def init():
    f[0] = 0
    f[1] = 1
    for i in range(2, 94):
        f[i] = f[i - 1] + f[i - 2]

if __name__ == "__main__":
    init()
    t = int(input())
    for i in range(t):
        a, b = map(int, input().split())
        for j in range(a, b + 1):
            print(f[j], end=" ")
        print()
    