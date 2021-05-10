import math
eps = 1e-5
n = int(input())
for i in range(n):
    m = int(input())
    ds = []
    for k in range(m):
        d = [float(dd) for dd in input().split()]
        ds.append(d)
    if m <= 2:
        print("0.000 0.000")
    else:
        x1 = ds[0][0]
        y1 = ds[0][1]
        x2 = ds[1][0]
        y2 = ds[1][1]
        x3 = 0
        y3 = 0
        sum_x = 0
        sum_y = 0
        sum_s = 0
        ds.pop(0)
        ds.pop(0)
        for b in ds:
            x3 = b[0]
            y3 = b[1]
            s = ((x2 - x1) * (y3 - y1) - (x3 - x1) * (y2 - y1)) / 2
            sum_x = sum_x + (x1 + x2 + x3) * s
            sum_y = sum_y + (y1 + y2 + y3) * s
            sum_s = sum_s + s
            x2 = x3
            y2 = y3
        if math.fabs(sum_s) <= eps:
            print("0.000 0.000")
        else:
            ddd = (sum_x / sum_s / 3) + (sum_y / sum_s / 3)
            df = "%.3f" % ddd
            if df == "-0.000":
                df = "0.000"
            print("%.3f %s" % (math.fabs(sum_s), df))
