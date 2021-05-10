try:
    while 1:
        n = [int(i) for i in input().split(":")]
        if n[0] == 0 and n[1] == 0:
            break
        n[0] = (n[0] * 30 + n[1] / 2)
        n[1] = n[1] * 6
        s = abs(n[0] - n[1])
        if s > 180:
            s = 360 - s
        print("%.3lf" % s)
except: pass