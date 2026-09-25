import re

n, k = map(int, input().split())
dicts = {}
for _ in range(n):
    arr = re.split("[^a-z0-9]", input().lower())
    for word in arr:
        if word != "":
            if word in dicts:
                dicts[word] += 1
            else:
                dicts[word] = 1
for x, y in sorted(dicts.items(), key=lambda item: (-item[1], item[0])):
    if y >= k:
        print(x + " " + str(y))