a, operator, b, equals, c = input().split()
a, b, c = map(int, (a, b, c))
if a + b == c:
    print("YES")
else:
    print("NO")