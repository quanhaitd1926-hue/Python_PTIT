s = input()
t = list(s)
low = 0
up = 0
for i in range(len(t)):
    if t[i].isupper():
        up += 1
    else: low += 1
if up > low: print(s.upper())
else: print(s.lower())