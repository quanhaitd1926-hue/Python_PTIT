n = int(input())
a = [input() for _ in range(n)]
ans = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 'C':
            for k in range(j + 1, n):
                if a[i][k] == 'C':
                    ans += 1
            for k in range(i + 1, n):
                if a[k][j] == 'C':
                    ans += 1
print(ans)