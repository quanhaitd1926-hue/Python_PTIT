n = input()
formatNumber = ""
cnt = 0
for i in range(len(n) - 1, -1, -1):
    cnt += 1
    formatNumber += n[i]
    if cnt % 3 == 0 and i != 0:
        formatNumber += ","
formatNumber = formatNumber[::-1]
print(formatNumber)