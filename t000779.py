import math
try:
    while 1:
        s = [int(i) for i in input().split()]
        if s[0] <= s[1]: print(2)
        else: print(math.ceil(s[0] * 2 / s[1]))
except: pass