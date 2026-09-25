t = int(input())
for _ in range(t):
    s = input()
    while True:
        formater = ""
        i = 0
        while i < len(s):
            j = i
            while j < len(s) and s[j] == s[i]:
                j += 1
            if j - i == 1:
                formater += s[i]
            i = j
        if formater == s:
            break
        s = formater
    print(s)