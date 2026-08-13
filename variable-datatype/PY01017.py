t = int(input())
for i in range(t):
	arr = input()
	arr += " "
	encode = ""
	cnt = 1
	tmp = arr[0]
	for i in range(1, len(arr)):
		if tmp == arr[i]:
			cnt += 1
		else:
			encode += str(cnt) + tmp
			cnt = 1
			tmp = arr[i]
	print(encode)	