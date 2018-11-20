import math
s = [int(i) for i in input().split()]
x = int(math.sqrt(2 * s[1]))
y = 0
while x >= 1:
    if 2 * s[1] % x == 0:
        y = int(2 * s[1] / x)
        if (x + y - 1) % 2 == 0:
            print("[%d,%d]" %(int((y - x + 1) / 2), int((x + y - 1) / 2)))
    x -= 1