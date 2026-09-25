my_set = set()
arr = list(input())
if len(arr) % 2 == 0:
    for i in range(0, len(arr), 2):
        s = arr[i] + arr[i + 1]
        x = int(s)
        my_set.add(s)
else:
    for i in range(0, len(arr) - 1, 2):
        s = arr[i] + arr[i + 1]
        x = int(s)
        my_set.add(x)
my_list = []
for x in my_set:
    my_list.append(x)

my_list.sort()
for x in my_list:
    print(x, end=" ")