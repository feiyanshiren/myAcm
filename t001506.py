try:
    while 1:
        a = [int(i) for i in input().split()]
        n = []
        for i in range(a[0]):
            s = [int(j) for j in input().split()]
            n.append(s)
        c = a[0] - a[1] + 1
        max = 0
        for i in range(c):
            for j in range(c):
                mm = 0
                for k in range(a[1]):
                    for l in range(a[1]):
                        mm += n[i + l][j + k]
                if mm > max:
                    max = mm
        print(max)
except:
    pass
    