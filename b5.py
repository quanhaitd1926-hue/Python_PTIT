def Try(i):
    global n, a, visited, b
    for j in range(n, 0, -1):
        if not visited[j]:
            a[i]=j
            visited[j] = True
            if i == n - 1:
                b.append("".join(map(str, a)))
            else:
                Try(i + 1)
            visited[j] = False

t = int(input())
for _ in range(t):
    n = int(input())
    a = [0] * n
    visited = [False] * (n + 1)
    b = []
    Try(0)
    print(len(b))
    print(" ".join(b))