while True:
    try:
        n = int(input())
        cnt = 1
        if n == 0: break
        else:
            while n != 1:
                if n % 2 == 0:
                    n /= 2
                    cnt += 1
                else:
                    n = n * 3 + 1
                    cnt += 1
            print(cnt)
    except EOFError:
        break