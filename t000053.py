n = int(input())
for i in range(n):
    zz = {}
    for j in range(1, 8):
        z = sum([int(k) for k in input().split()])
        if z > 8:
            f = 0
            for k, v in zz.items():
                if v == z:
                    f = 1
            if f == 1:
                continue
            zz[j] = z
    if len(zz) != 0:
        d = sorted(zz.items(), key=lambda d: d[1])
        if d[-1][1] > 8:
            print(d[-1][0])
        else:
            print(0)
    else:
        print(0)
