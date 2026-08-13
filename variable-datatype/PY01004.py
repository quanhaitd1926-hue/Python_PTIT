import math

def prime(n):
    if n < 2:
        return False

    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False

    return True


if __name__ == '__main__':
    t = int(input())

    for _ in range(t):
        n = int(input())

        k = 0

        for i in range(1, n):
            if math.gcd(i, n) == 1:
                k += 1

        if prime(k):
            print("YES")
        else:
            print("NO")