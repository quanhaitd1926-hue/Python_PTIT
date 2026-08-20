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
        if not isPrime(len(n)): print("NO")
        else:
            cnt = 0
            for j in range(len(n)):
                if n[j] == "2" or n[j] == "3" or n[j] == "5" or n[j] == "7": cnt += 1
            if cnt > len(n) - cnt: print("YES")
            else: print("NO")