n = int(input())
for i in range(n):
    a = [[0, 0], [0, 0], [0, 0], [0, 0]]
    b = [0, 0]
    c = [0, 0]
    d = [0, 0]
    z = [int(j) for j in input().split()]
    a[0][0] = z[0]
    a[0][1] = z[1]
    a[1][0] = z[2]
    a[1][1] = z[3]
    a[2][0] = z[4]
    a[2][1] = z[5]
    a[3][0] = z[6]
    a[3][1] = z[7]
    b[0] = a[1][0] - a[0][0]
    b[1] = a[1][1] - a[0][1]
    c[0] = a[2][0] - a[0][0]
    c[1] = a[2][1] - a[0][1]
    d[0] = a[3][0] - a[0][0]
    d[1] = a[3][1] - a[0][1]
    e = b[0]*c[1] - b[1]*c[0]
    f = c[0]*d[1] - c[1]*d[0]
    if e < 0:
        e = -e
    if f < 0:
        f = -f
    g = e + f
    h1 = e / g
    h2 = 1 - h1
    x = b[0] * h2 + d[0] * h1
    y = b[1] * h2 + d[1] * h1
    x += a[0][0]
    y += a[0][1]
    print("%.2f %.2f" % (x, y))
