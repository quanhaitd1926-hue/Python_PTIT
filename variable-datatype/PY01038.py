t = int(input())
for i in range(t):
    n = input()
    if int(n) % 7 == 0: print(n)
    else:
        cnt = 0
        check = False
        while cnt < 1000:
            reverse_n = n[::-1]
            total = int(n) + int(reverse_n)
            if total % 7 == 0:
                print(total)
                check = True
                break
            n = str(total)
            cnt += 1
        if check == False: print("-1")