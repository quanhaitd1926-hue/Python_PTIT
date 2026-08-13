n = int(input())
cnt = 0
while n != 0:
    q = n % 10
    if q == 4 or q == 7:
        cnt += 1
    n //= 10
if cnt == 4 or cnt == 7:
    print("YES")
else:
    print("NO")
