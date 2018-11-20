try:
    while 1:
        n = int(input())
        s = {i + 1: int(j) for i, j in enumerate(input().split())}
        p = sorted(s.items(), key=lambda d: d[1])
        ma = 0
        id = []
        for i in range(len(p) - 2):
            a = p[i][1] + p[i+1][1] + p[i+2][1]
            if a > ma:
                id = [p[i], p[i+1], p[i+2]]
                ma = a
            else: break
        d = sorted(id, key=lambda d: d[0])
        print("%d %d %d %d" % (d[0][0], d[1][0], d[2][0], ma))
except: pass