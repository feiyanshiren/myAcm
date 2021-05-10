try:
    z = 0
    while 1:
        z += 1
        n = [int(i) for i in input().split()]
        k1 = 1
        k2 = 2
        if n[0] % 2 == 0:
            k1 , k2 = k2, k1
        x1 = n[1] + 2 ** (n[0] - k1)
        x2 = n[1] + 2 ** (n[0] - k2)
        print("case #%d: %d %d" % (z, x1, x2))
except:
    pass