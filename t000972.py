import math
try:
    while 1:
        s = [int(i) for i in input().split()]
        c = 1
        for i in s:
            if i != 0: c = int((c * i) / math.gcd(c, i))
        print(c * len(s))
except: pass


