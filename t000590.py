try:
    while 1:
        y = [int(i) for i in input().split()]
        e = [int(i) for i in input().split()]
        c = 0
        for i in range(y[0]):
            s = 0
            j = i
            while s < y[1] and j < y[0]:
                s += e[j]
                j += 1
            if s == y[1]:
                c += 1
        print(c)
except: pass