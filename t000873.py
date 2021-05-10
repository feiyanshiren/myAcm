try:
    while 1:
        d = [int(i) for i in input().split()]
        a = [int(i) for i in input().split()]
        s = 0
        m = 0
        b = 0
        e = 0
        for i in range(d[0]):
            for j in range(i, i + d[1]):
                s += a[j % d[0]]
            if s > m:
                m = s
                b = i + 1
                e = (i + d[1] - 1) % d[0] + 1
            s = 0
        print("%d %d %d" % (m, b, e))
except: pass