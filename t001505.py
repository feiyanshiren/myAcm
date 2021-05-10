try:
    while 1:
        n = int(input())
        s = [int(i) for i in input().split()]
        if len(s) < 2:
            s.append(0)
        m = s[1] - s[0]
        for i in range(2, n):
            m = max(m, s[i] - s[i - 1])
        print("%d.00" % m)
except:
    pass