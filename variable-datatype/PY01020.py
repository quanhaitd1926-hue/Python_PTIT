t = int(input())
for i in range(t):
    s = input()
    loc_phat = s[len(s) - 2] + s[len(s) - 1]
    loc_phat = int(loc_phat)
    if loc_phat == 86: print("YES")
    else: print("NO")