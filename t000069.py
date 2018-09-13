import math
n = int(input())
for i in range(n):
    s = int(input())
    r = 0
    for j in range(1, s + 1):
        r = r + math.log10(j)
    print(int(r) + 1)
