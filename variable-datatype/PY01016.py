t = int(input())
for i in range(t):
	arr = list(input())
	for i in range(0, len(arr), 2):
		cnt = int(arr[i + 1])
		for j in range(cnt):
			print(arr[i], end="")
	print()