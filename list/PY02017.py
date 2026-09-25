t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    d = {}
    for x in arr:
        if x in d:
            d[x] += 1
        else: d[x] = 1
    for k, v in d.items():
        if v % 2 != 0:
            print(k)
            break