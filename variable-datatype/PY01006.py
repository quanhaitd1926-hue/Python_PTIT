def check(n):
    while n != 0:
        q = n % 10
        if q != 4 and q != 7:
            return False
        n //= 10
    return True
    
if __name__ == '__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        if check(n): print("YES")
        else: print("NO")