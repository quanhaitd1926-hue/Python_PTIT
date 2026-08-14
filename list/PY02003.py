import math

def isListHamming(n):
    for i in [2, 3, 5]:
        while n % i == 0:
            n //= i

    return n == 1

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        if isListHamming(n): print(n)
        else: print("Not in sequence")