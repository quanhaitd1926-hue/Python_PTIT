digits = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
t = int(input())
for i in range(t):
    n, b = map(int, input().split())
    res = ""

    while n > 0:
        remainder = n % b
        res += digits[remainder]
        n //= b

    print(res[::-1])