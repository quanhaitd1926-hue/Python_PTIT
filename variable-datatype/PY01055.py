t = int(input())
for i in range(t):
    n = input()
    if len(n) % 2 == 0: print("NO")
    else:
        if n[0] == n[1]: print("NO")
        else:
            check = True
            for j in range(2, len(n), 2):
                if n[j] != n[j - 2]:
                    check = False
                    break
            if check: print("YES")
            else: print("NO")