import math
for m in range(int(input())):
    input()
    r = [float(i) for i in input().split()]
    r.sort(reverse=True)
    l = 0
    c = 0
    while l < 10:
        l += math.sqrt(r.pop(0) ** 2 - 1)
        c += 1
    print(c)
