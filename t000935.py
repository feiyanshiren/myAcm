import math
for t in range(int(input())):
    n = int(input())
    d = int(math.sqrt(n))
    k = 0
    for i in range(d, 0, -1):
        if n % i == 0 and (int(n / i) != i) and (int(n / i - i) % 2 == 0):
            print(int((n / i - i) / 2))
            k = 1
            break
    if k == 0: print(-1)