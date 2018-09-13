import math
f = {
    "W": [-1, 0], "E": [1, 0],
    "N": [0, 1], "S": [0, -1]
}
try:
    while 1:
        m1 = input().split()
        m2 = input().split()
        r1 = [0, 0]
        r2 = [0, 0]
        for mm1 in m1:
            r1[0] = r1[0] + f[mm1][0]
            r1[1] = r1[1] + f[mm1][1]
        for mm2 in m2:
            r2[0] = r2[0] + f[mm2][0]
            r2[1] = r2[1] + f[mm2][1]
        d = math.sqrt(((r2[1] - r1[1]) ** 2) + ((r2[0] - r1[0]) ** 2))
        print("%.2f" % d)
except Exception:
    pass
