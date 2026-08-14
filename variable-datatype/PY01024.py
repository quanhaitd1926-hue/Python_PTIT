import math

def check(n):
    sum = 0
    for i in range(len(n) - 1):
        a = int(n[i])
        b = int(n[i + 1])
        if abs(b - a) != 2: return False
        sum += a
    sum += int(n[len(n) - 1])
    if sum % 10 != 0: return False
    return True

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = input()
        if check(n): print("YES")
        else: print("NO")