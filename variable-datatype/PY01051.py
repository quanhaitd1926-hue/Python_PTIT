def isPalindrome(n):
    l = 0
    r = len(n) - 1
    while l <= r:
        if n[l] != n[r]: return False
        l += 1
        r -= 1
    return True

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
        if len(str(total)) <= 1: print("NO")
        else:
            if isPalindrome(str(total)): print("YES")
            else: print("NO")