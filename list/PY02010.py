while True:
    n = int(input())
    arr = []
    if n == 0: break
    for i in range(0, n):
        arr.append(int(input()))
    arr.sort()
    min_value = arr[0]
    max_value = arr[len(arr) - 1]
    if min_value == max_value: print("BANG NHAU")
    else: print(f"{min_value} {max_value}")
    