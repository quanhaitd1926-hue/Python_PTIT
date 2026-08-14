import math

def analysis(n):
    analysisPrime = "1"
    for i in range(2, int(math.sqrt(n) + 1)):
        cnt = 0
        if n % i == 0:
            while n % i == 0:
                cnt += 1
                n //= i
            analysisPrime += " * " + str(i) + "^" + str(cnt)
    if n != 1: analysisPrime += " * " + str(n) + "^" + "1"
    return analysisPrime
        
        
if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = int(input())
        print(analysis(n))