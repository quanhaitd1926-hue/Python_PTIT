t = int(input())
for i in range(1, t + 1):
    s1 = input()
    s2 = input()
    check = True
    if len(s1) != len(s2):
        print("Test " + str(i) + ": ", end="")
        print("NO")
        continue
    s1 = "".join(sorted(s1))
    s2 = "".join(sorted(s2))
    print("Test " + str(i) + ": ", end="")
    if s1 == s2: print("YES")
    else: print("NO")
    