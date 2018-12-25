import math
for T in range(int(input())):
    s = [int(i) for i in input().split()]
    c = s[0] * (100 - s[1]) + 100 * (100 - s[0])
    d = s[0] * (100 - s[1])
    e = 10000 - s[0] * 100
    q = math.gcd(d, c)
    w = math.gcd(e, c)
    print("%d/%d %d/%d" % (d/q, c/q, e/w, c/w))