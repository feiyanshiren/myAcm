for t in range(int(input())):
    zs = []
    ts = input().split()
    if len(ts) != 0:
        ts2 = [int(g) for g in ts]
        zs.append(ts2)
        for i in range(6):
            s = [int(d) for d in input().split()]
            zs.append(s)
    else:
        for i in range(7):
            s = [int(d) for d in input().split()]
            zs.append(s)
    z = 0
    for i in range(5):
        for k in range(5):
            if zs[i + 1][k + 1] == 1:
                a = zs[i][k + 1]
                b = zs[i + 1][k]
                c = zs[i + 2][k + 1]
                d = zs[i + 1][k + 2]
                if a == 1 and b == 1 and c == 1 and d == 1:
                    z = z + 1
            else:
                continue
    print(z)
