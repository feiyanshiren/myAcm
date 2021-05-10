import math
pi = 3.14159265
xx = 0.00001
try:
    while 1:
        s = [float(i) for i in input().split()]
        if abs(s[4]) <= xx:
            print("%.1f %.1f" % (s[2], s[3]))
            continue
        angle = pi / 180 * (s[4])
        x3 = (s[2] - s[0]) * math.cos(angle) -\
             (s[3] - s[1]) * math.sin(angle) + s[0]
        y3 = (s[2] - s[0]) * math.sin(angle) +\
             (s[3] - s[1]) * math.cos(angle) + s[1]
        print("%.1f %.1f" % (x3, y3))
except EOFError:
    pass
