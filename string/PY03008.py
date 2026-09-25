n = int(input())
degree = [0] * (n + 1)
for i in range(0, n - 1):
    u, v = map(int, input().split())
    degree[u] += 1
    degree[v] += 1
check = True
cnt = 0
for i in range(1, n + 1):
    if degree[i] == n - 1:
        cnt += 1
    elif degree[i] != 1:
        check = False
        break
if check and cnt == 1:
    print("Yes")
else:
    print("No")
        