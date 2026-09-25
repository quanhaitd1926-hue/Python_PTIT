from math import *
from collections import *

n = int(input())

a = []
for i in range(n):
    line = input().split()
    new_line = []
    for x in line:
        new_line.append(int(x))
    a.append(new_line)
k = int(input())

sum_u = 0
sum_l = 0
for i in range(n):
    for j in range(n):
        if i + j < n - 1:
            sum_u = sum_u + a[i][j]
        elif i + j > n - 1:
            sum_l = sum_l + a[i][j]
c = sum_u - sum_l
if c < 0:
    c = -c
if c <= k: print("YES")
else: print("NO")
print(c)