n = int(input())
m = int(input())
ke = []
for i in range(n + 1):
    row = []
    for j in range(n + 1):
        row.append(False)
    ke.append(row)

degree = []
for i in range(n + 1):
    degree.append(0)
for i in range(m):
    line = input().split()
    u = int(line[0])
    v = int(line[1])
    if ke[u][v] == False:
        ke[u][v] = True
        ke[v][u] = True
        degree[u] = degree[u] + 1
        degree[v] = degree[v] + 1

vis = []
for i in range(n + 1):
    vis.append(False)
comp = 0
ok = True
for i in range(1, n + 1):
    if vis[i] == False:
        comp += 1
        q = [i]
        vis[i] = True
        tp = [i]
        dau = 0
        while dau < len(q):
            u = q[dau]
            dau += 1
            for v in range(1, n + 1):
                if ke[u][v] == True and vis[v] == False:
                    vis[v] = True
                    q.append(v)
                    tp.append(v)
        kt = len(tp)
        for j in range(len(tp)):
            dinh = tp[j]
            if degree[dinh] != kt - 1:
                ok = False
if comp <= 2 and ok == True: print("YES")
else: print("NO")


