t = int(input())
for i in range(t):
    arr = list(input())
    check = True
    for i in range(1, len(arr)):
        a, b = map(int, (arr[i - 1], arr[i]))
        if a > b:
            check = False
            break
    if check: print("YES")
    else: print("NO")