s1 = list(input())
s2 = input()
p = int(input())
p -= 1
s1.insert(p, s2)
s = ''.join(s1)
print(s)
