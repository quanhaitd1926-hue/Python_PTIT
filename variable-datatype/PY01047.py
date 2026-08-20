import math

def isPrime(n):
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = input()
        s = n[len(n) - 4 : len(n)]
        if isPrime(int(s)): print("YES")
        else: print("NO")