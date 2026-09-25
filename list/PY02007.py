setCnt = set()
while True:
    try:
        line = input()
        if line == "": break
        arr = list(map(int, line.split()))
        for i in range(len(arr)):
            setCnt.add(arr[i] % 42)
    except EOFError:
        break

print(len(setCnt))
