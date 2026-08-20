def generate(limit):
    res = []

    def dfs(s, length):
        if len(s) == length:
            num = int(s + s[::-1])

            if num <= limit:
                res.append(num)

            return

        for d in "02468":
            if len(s) == 0 and d == "0":
                continue

            dfs(s + d, length)

    for length in range(1, len(str(limit)) // 2 + 1):
        dfs("", length)

    return sorted(res)


t = int(input())
arr = []

for _ in range(t):
    arr.append(int(input()))

max_n = max(arr)
numbers = generate(max_n)

for n in arr:
    for x in numbers:
        if x > n:
            break
        print(x, end=" ")
    print()