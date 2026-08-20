import math

l, r = map(int, input().split())
for i in range(l, r + 1):
    for j in range(i + 1, r + 1):
        for k in range(j + 1, r + 1):
            if math.gcd(i, j) == 1 and math.gcd(i, k) == 1 and math.gcd(j, k) == 1:
                print("(" + str(i) + ", " + str(j) + ", " + str(k) + ")")