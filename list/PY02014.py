import math
import sys

listPrime = []

def isPrime(n):
    if n <= 1: return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0: return False
    return True

def init():
    for i in range(10001):
        if isPrime(i): listPrime.append(i)

if __name__ == "__main__":
    init()
    my_list = []
    n = int(input())
    arr = list(map(int, input().split()))
    for i in range(n):
        if isPrime(arr[i]): continue
        l = -1
        r = -1
        min_value = sys.maxsize
        for j in range(len(listPrime)):
            if arr[i] - listPrime[j] < 0:
                l = j - 1
                r = j
                break
        if l >= 0:
            if min_value > arr[i] - listPrime[l]:
                min_value = arr[i] - listPrime[l]
        if r >= 0:
            if min_value > -arr[i] + listPrime[r]:
                min_value = -arr[i] + listPrime[r]  
        my_list.append(min_value)
    if len(my_list) != 0:
        my_list.sort(reverse=True)
        print(my_list[0])
    else: print(0)
