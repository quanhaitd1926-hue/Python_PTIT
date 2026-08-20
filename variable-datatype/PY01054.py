t = int(input())
for i in range(t):
    n = input()
    s = 1
    for j in range(len(n)):
        if n[j] == "0": continue
        s *= int(n[j])
    print(s)