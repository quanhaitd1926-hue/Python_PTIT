a, k, n = map(int, input().split())

first = ((a // k) + 1) * k

if first > n:
	print(-1)
else:
	for i in range(first, n + 1, k):
		print(i - a, end = " ")