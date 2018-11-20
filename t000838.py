try:
    while 1:
        s = [float(i) for i in input().split()]
        if s[0] == 0.0 and s[1] == 0.0: print("0.00")
        elif s[0] == 0.0: print("%.2f" % s[1])
        elif s[1] == 0.0: print("%.2f" % s[0])
        else: print("%.2f" % (s[0] * s[1] / (s[0] + s[1])))
except: pass