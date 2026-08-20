import math

def isPrime(n):
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def caculatorTotal(n):
    total = 0
    for i in range(len(n)):
        total += int(n[i])
    return total

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = input()
        total = caculatorTotal(n)
        if not isPrime(total): print("NO")
        else:
            check = True
            for j in range(len(n)):
                if j % 2 == 0:
                    if int(n[j]) % 2 != 0:
                        check = False
                        break
                else:
                    if int(n[j]) % 2 == 0:
                        check = False
                        break
            if check: print("YES")
            else: print("NO")