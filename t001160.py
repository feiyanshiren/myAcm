import math
def gbd(a, b):
    return (a * b) // math.gcd(a, b) 
try:
    while 1:
        n = int(input())
        s = [int(i) for i in input().split()]
        m = n // s[0] - n // gbd(s[0], s[1]) +\
            n // s[1] - n // gbd(s[1], s[2]) +\
            n // s[2] - n // gbd(s[0], s[2]) +\
            n // gbd(gbd(s[0], s[1]), s[2])
        print(n - m)
except:
    pass
