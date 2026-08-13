t = int(input())
for i in range(t):
    s = input()
    code = ""
    sum = 0
    for i in range(len(s)):
        if s[i].isdigit():
            sum += int(s[i])
        else: code += s[i]
    code = "".join(sorted(code))
    code += str(sum)
    print(code)