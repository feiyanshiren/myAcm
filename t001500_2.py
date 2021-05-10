try:
    while 1:
        x = "*"
        n = [int(i) for i in input().split()]
        b = " " * (n[1] // 2 - 1)
        c = x * n[1]
        k = "%s%s%s%s%s" % (x, b, x, b, x)
        print(c)
        w = n[0] // 2 - 1
        for i in range(w):
            print(k)
        print(c)
        for i in range(w):
            print(k)
        print(c)
        print()
except:
    pass
