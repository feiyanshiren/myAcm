t = 0
try:
    while 1:
        s = [i for i in input().split()]
        d = float(s[1]) * float(s[2])
        t += d
except:
    print("%.1f" % t)
    