def checkList(a, b, n):
    for i in range(n):
        if a[i] > b[i]: return False
    return True

if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        n = int(input())
        a = list(map(int, input().split()))
        b = list(map(int, input().split()))
        a.sort()
        b.sort()
        if checkList(a, b, n): print("YES")
        else: print("NO")