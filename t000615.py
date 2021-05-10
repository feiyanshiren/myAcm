try:
    while True:
        z = {}
        n = int(input())
        ss = [int(s) for s in input().split()]
        ss.sort()
        for i in range(len(ss) - 1):
            d = abs(ss[i] - ss[i + 1])
            if d not in z.keys():
                z[d] = i
        k = sorted(z.keys())[0]
        i = z[k]
        print("%d %d" % (ss[i], ss[i + 1]))
except EOFError:
    pass
