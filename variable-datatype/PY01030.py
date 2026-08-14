import math

n, k = map(int, input().split())
min_value = int(math.pow(10, k - 1))
max_value = int(math.pow(10, k)) - 1

cnt = 0
for i in range(min_value, max_value + 1):
    if math.gcd(n, i) == 1:
        print(i, end=" ")
        cnt += 1
    if cnt == 10:
        print()
        cnt = 0