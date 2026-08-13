P = "ABCDEFGHIJKLMNOPQRSTUVWXYZ_."
while True:
    string = input()
    if len(string) == 1: break
    k, s = string.split()
    k = int(k)
    code = ""
    for i in range(len(s)):
        index = -1
        for j in range(len(P)):
            if s[i] == P[j]:
                index = j
                break
        code += P[(j + k) % 28]
    reverse_code = code[::-1]
    print(reverse_code)