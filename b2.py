t = int(input())
for _ in range(t):
    arr = input().split()
    prefix = arr[0]
    for s in arr:
        while not s.startswith(prefix):
            prefix = prefix[:-1]
    print(prefix)