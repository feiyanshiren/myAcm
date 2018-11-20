import math
for N in range(int(input())):
    s = [float(i) for i in input().split()]
    a = math.sqrt((s[2] - s[0]) ** 2 + (s[3] - s[1]) ** 2)
    b = math.sqrt((s[4] - s[2]) ** 2 + (s[5] - s[3]) ** 2)
    c = math.sqrt((s[4] - s[0]) ** 2 + (s[5] - s[1]) ** 2)
    if (a + b) > c and (a + c) > b and (b + c) > a:
        p = a + b + c
        s = (math.sqrt(p * (p - 2 * a) * (p - 2 * b) * (p - 2 * c))) / 4
        print("%.3f" % s)
    else: print("Can not form a triangle.")