Octal = ["000", "001", "010", "011", "100", "101", "110", "111"]

binary_string = input()
first = 0
if len(binary_string) % 3 != 0:
    first = ((len(binary_string) // 3) + 1) * 3
for i in range(0, first - len(binary_string)):
    binary_string = "0" + binary_string
cnt = 0
while cnt < len(binary_string):
    res = binary_string[cnt : cnt + 3]
    for i in range(len(Octal)):
        if res == Octal[i]: print(i, end="")
    cnt += 3