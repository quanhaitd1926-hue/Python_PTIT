while True:
    try:
        arr = list(map(int, input().split()))
        if arr == [0, 0, 0, 0]:
            break
        cnt = 0
        while len(set(arr)) != 1:
            arr2 = [0] * 4
            for i in range(3):
                arr2[i] = abs(arr[i] - arr[i + 1])
            arr2[3] = abs(arr[3] - arr[0])
            arr = arr2
            cnt += 1
        print(cnt)
    except EOFError:
        break