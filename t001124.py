try:
    while 1:
        nm = [int(i) for i in input().split()]
        n = [int(i) for i in input().split()]
        a = [0]
        b = [0]
        for i in n:
            if i == 0:
                a.append(a[-1] + 0)
                b.append(b[-1] + 0)
            elif i > 0:
                a.append(a[-1] + 1)
                b.append(b[-1] + 0)
            else:
                a.append(a[-1] + 0)
                b.append(b[-1] + 1)
        for i in range(nm[1]):
            m = [int(j) for j in input().split()]
            y = a[m[1]] - a[m[0] - 1]
            my = b[m[1]] - b[m[0] - 1]
            print("%d %d" % (y, my))
except EOFError:
    pass
