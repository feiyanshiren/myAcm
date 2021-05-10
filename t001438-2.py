try:
    while 1:
        h = [float(i) for i in input().split()]
        print("%.6f" % (3 * h[0] * h[2] ** 2 + h[1]))
except:
    pass