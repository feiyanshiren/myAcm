def fe(n1, n2):
    z = abs(n1 - n2)
    if z < 1.0e-9:
        return True
    else:
        return False


n = int(input())
for i in range(n):
    k = int(input())
    z = 1 / k
    zd = k * (k + 1)
    zx = k * 2
    d = []
    for j in range(zd, zx - 1, -1):
        z1 = 1 / j
        for o in range(1, zx + 1):
            z2 = 1 / o
            if fe(z1 + z2, z):
                d.append([j, o])
    for j in d:
        s = "1/%d=1/%d+1/%d" % (k, j[0], j[1])
        print(s)
