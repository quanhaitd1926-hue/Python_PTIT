def caculatorTotal(n):
    total = 0
    for i in range(len(n)):
        total += int(n[i])
    return total

if __name__ == "__main__":
    t = int(input())
    for i in range(t):
        n = input()
        total = caculatorTotal(n)
        if total % 3 == 0: print("YES")
        else: print("NO")