import sys

n = int(input())
arr = list(map(int, input().split()))
min_value = sys.maxsize
index = -1
for i in range(n):
    total = 0
    for j in range(n):
        if arr[i] > arr[j]: total += arr[i] - arr[j]
        else: total += arr[j] - arr[i]
    if total < min_value:
        min_value = total
        index = i
print(f"{min_value} {arr[index]}")