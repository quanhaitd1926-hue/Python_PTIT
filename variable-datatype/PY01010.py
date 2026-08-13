t = int(input())
for i in range(t):
    n = list(input())
    n1 = n[0] + n[1]
    n2 = n[len(n) - 2] + n[len(n) - 1]
    if int(n1) == int(n2): print("YES")
    else: print("NO")