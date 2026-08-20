t = int(input())
for i in range(t):
	n = int(input())
	total = 0.0
	if n % 2 == 0:
		for j in range(2, n + 1, 2):
			total += 1.0 / j
	else:
		for j in range(1, n + 1, 2):
			total += 1.0 / j
	print(f"{total:.6f}")