import math
for m in range(int(input())):
    n = int(input())
    r = [float(i) for i in input().split()]
    r.sort()
    l = 0
    c = 0
    while l < 20:
        a = r.pop(-1)
        l += 2 * math.sqrt(a ** 2 - 1)
        c += 1
    print(c)
