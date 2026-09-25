import math

p = [1] * 1000001
arrPrime = []

def sang():
    p[0] = p[1] = 0
    for i in range(2, int(math.sqrt(1000001)) + 1):
        if p[i] == 1:
            for j in range(i * i, 1000001, i):
                p[j] = 0

def initPrime():
    for i in range(1000001):
        if p[i] == 1: arrPrime.append(i)

if __name__ == "__main__":  
    sang()
    initPrime()
    n, x = map(int, input().split())
    print(x, end=" ")
    for i in range(n):
        x += arrPrime[i]
        print(x, end=" ")
