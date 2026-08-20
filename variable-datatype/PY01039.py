t = int(input())
for i in range(t):
    n = input()
    my_set = set()
    for j in range(len(n)):
        my_set.add(n[j])
    if len(my_set) != 2: print("NO")
    else:
        isBeautiful = True
        for j in range(1, len(n)):
            if n[j] == n[j - 1]:
                isBeautiful = False
                break
        if isBeautiful: print("YES")
        else: print("NO")