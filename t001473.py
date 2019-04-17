try:
    while 1:
        F = [int(i) for i in input().split()]
        ns = {}
        for T in range(F[1]):
            N = [int(i) for i in input().split()]
            ns[N[1]] = ns.get(N[1], 0) + N[0]
        kk = sorted(ns.items(), key=lambda d: d[0], reverse=True)
        z = 0
        for i in kk:
            m = min(F[0], i[1])
            z += m * i[0]
            F[0] = F[0] - m
            if F[0] <= 0:
                break
        print(z)
except:
    pass
