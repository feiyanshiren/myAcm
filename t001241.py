try:
    while 1:
        n = [int(i) for i in input().split()]
        f = [0 for i in range(111)]
        a = []
        b = []
        s = []
        t = []
        for i in range(n[0]):
            d = [int(j) for j in input().split()]
            a.append(d[0])
            b.append(d[1])
        for i in range(n[1]):
            d = [int(j) for j in input().split()]
            s.append(d[0])
            t.append(d[1])
        for i in range(n[1]):
            for j in range(n[0]):
                if a[j] > s[i] and b[j] > t[i] or a[j] < s[i] and b[j] < t[i]:
                    f[i] = f[i] + 1
                else:
                    f[i] = f[i] - 1
        for i in range(n[1]):
            print(f[i])
except:
    pass