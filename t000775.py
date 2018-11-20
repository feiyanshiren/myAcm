def ee(a, b, xyq):
    if b == 0:
        xyq[0] = 1
        xyq[1] = 0
        xyq[2] = a
    else:
        ee(b, a % b, xyq)
        t = xyq[0]
        xyq[0] = xyq[1]
        xyq[1] = t - int(a / b) * xyq[1]
try:
    while 1:
        s = input().split()
        xyq = [0, 0, 0]
        ee(int(s[0]), int(s[1]), xyq)
        print("%d %d" % (xyq[0], xyq[1]))
except: pass