import math
for N in range(int(input())):
    s = [int(i) for i in input().split()]
    a = []
    for n in range(s[0]):
        t = [int(i) for i in input().split()]
        d = math.sqrt(t[1] ** 2 - (s[2] / 2) ** 2) if t[1] >= s[2] / 2 else 0
        if d != 0:
            u = [t[0] - d, t[0] + d]
            a.append(u)
    a.sort(key=lambda x: x[0])
    b = []
    d = 0
    b.append(a.pop(0))
    d += b[0][1] - b[0][0]
    c = 1
    while d < s[1]:
        e = []
        f = a[0]
        while f[0] <= b[-1][1] and f[1] >= b[-1][0]:
            e.append(f)
            a.pop(0)
            if len(a) != 0:
                f = a[0]
            else:
                break
        e.sort(key=lambda x: x[1])
        t = e[-1]
        b.append(t)
        d += t[1] - t[0]
        c += 1
    print(c)
