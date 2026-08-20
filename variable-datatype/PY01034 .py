def swap(text, idx1, idx2):
	char_list = list(text)
	char_list[idx1], char_list[idx2] = char_list[idx2], char_list[idx1]
	return ''.join(char_list)

if __name__ == "__main__":
	t = int(input())
	for i in range(t):
		n = input()
		index = -1
		for j in range(len(n) - 1, 0, -1):
			if n[j] < n [j - 1]:
				index = j - 1
				break
		if index == -1: print(-1)
		else:
			max_value = -1
			idx = -1
			for j in range(index + 1, len(n)):
				if int(n[j]) > max_value and n[j] < n[index]:
					max_value = int(n[j])
					idx = j
			res = swap(n, index, idx)
			if(res[0] == "0"): print("-1")
			else: print(res)
		