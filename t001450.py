import math
def is_prime(val):
    if val < 2:
        return 0
    k = int(math.sqrt(val))
    for i in range(2, k + 1):
        if val % i == 0:
            return 0
    return 1

try:
    while 1:
        n = int(input())
        f = 0
        a = 0
        if is_prime(n):
            if not f:
                print("YES")
            f = 1
            print(n)
        while(n // 10):
            t = n
            while t:
                tmp = t % 10
                a += tmp
                t //= 10
            n = a
            if is_prime(a):
                if not f:
                    print("YES")
                f = 1
                print(a)
            a = 0
        if not f:
            print("NO")
except:
    pass
