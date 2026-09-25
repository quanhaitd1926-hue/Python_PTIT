import sys

n = int(input())
arr = list(map(int, sys.stdin.read().split()))
listEven = []
listOdd = []
for i in range(n):
    if arr[i] % 2 == 0: listEven.append(arr[i])
    else: listOdd.append(arr[i])
listEven.sort()
listOdd.sort(reverse=True)
indexEven = 0
indexOdd = 0
for i in range(n):
    if arr[i] % 2 == 0:
        print(listEven[indexEven], end=" ")
        indexEven += 1
    else:
        print(listOdd[indexOdd], end=" ")
        indexOdd += 1