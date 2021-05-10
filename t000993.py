import math
try:
    while 1:
        n = [int(i) for i in input().split()]
        if n[1] != n[2]: print((n[0] - 1) // n[1] + (n[0] - 1) // n[2] - (n[0] - 1) // ((n[1] * n[2]) // math.gcd(n[1], n[2])))
        else: print((n[0] - 1) // n[1])
except: pass