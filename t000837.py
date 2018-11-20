import math
def d(a, b):
    for i in range(100001):
        a.append(int(i * (1.0 + math.sqrt(5.0)) / 2))
        b.append(a[i] + i)
a = []
b = []
d(a, b)
try:
    while 1:
        for n in range(int(input()) + 1): print("(%d,%d)" % (a[n], b[n]), end="")
        print()
except: pass
