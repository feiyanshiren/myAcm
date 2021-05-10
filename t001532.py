for T in range(int(input())):
    n = [int(i) for i in input().split()]
    a = []
    b = {}
    for j in range(n[0]):
        p = [int(i) for i in input().split()]
        a.append(p)
    for j in range(n[1]):
        q = [float(i) for i in input().split()]
        if q[1] > b.get(int(q[0]), 0):
            b[int(q[0])] = q[1]
    c = []
    for i in a:
        z = 1
        for j in range(2, i[1] + 2):
            z += b[i[j]]
        z *= i[0]
        c.append(z)
    print("%.4f" % max(c))
