t = int(input())
for i in range(t):
    n = input()
    cnt = len(n)
    if cnt < 3: print("NO")
    else:
        l = 0
        r = len(n) - 1
        while l < r and cnt >= 0:
            if n[l] < n[l + 1]: l += 1
            if n[r] < n[r - 1]: r -= 1
            cnt -= 1
        if l == r: print("YES")
        else: print("NO")