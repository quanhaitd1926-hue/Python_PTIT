n = int(input())
arr = list(map(int, input().split()))

my_set = set(arr)

for i in range(1, n + 2):
    if i not in my_set:
        print(i)
        break