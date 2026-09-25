t = int(input())
for _ in range(t):
    n = int(input())
    arr = list(map(int, input().split()))
    d = {}
    for x in arr:
        if x in d:
            d[x] += 1
        else: d[x] = 1
    my_list = []
    max_value = -1
    for k, v in d.items():
        if max_value < v and v > n / 2:
            max_value = v
    if max_value == -1: print("NO")
    else:
        for k, v in d.items():
            if max_value == v:
                my_list.append(k)
        my_list.sort()
        print(my_list[0])