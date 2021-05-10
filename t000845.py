z = []
while 1:
    s = [int(i) for i in input().split()]
    if s[0] == 0 and s[1] == 0:
        f = {}
        for zz in z:
            if zz[0] in f.keys():
                f[zz[0]] = f[zz[0]] + zz[1]
            else:
                f[zz[0]] = zz[1]
        for i in f.keys():
            print("%d %d" % (i, f[i]))
        break
    else:
        z.append(s)
