import math

t = int(input())
for i in range(t):
    n = input()
    reverse_n = n[::-1]
    if math.gcd(int(n), int(reverse_n)) == 1: print("YES")
    else: print("NO")