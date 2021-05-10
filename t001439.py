import math
try:
    while 1:
        s = [float(i) for i in input().split()]
        cc = (s[0] ** 2 + s[1] ** 2 - s[2] ** 2) / (2 * s[0] * s[1])
        print("%.3f" % math.acos(cc))
except:
    pass