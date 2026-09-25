t = int(input())
for _ in range(t):
    hmap = {}
    n = int(input())
    for i in range(n):
        tmp = int(input())
        if tmp in hmap:
            hmap[tmp] += 1
        else: hmap[tmp] = 1
    for x, y in sorted(hmap.items(), key=lambda item: (-item[1], item[0])):
        print(x)
        break
