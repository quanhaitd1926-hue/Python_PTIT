a = set(input().lower().split())
b = set(input().lower().split())
print(*sorted(a|b))
print(*sorted(a&b))