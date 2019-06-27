for n in range(int(input())):
    m = int(input())
    x = []
    y = []
    for i in range(m):
        s = input().split()
        x.append(int(s[0]))
        y.append(int(s[1]))
    x.sort()
    y.sort()
    u = []
    for i in range(m):
        x1 = x[i]
        y1 = y[i]
        k = 0
        for j in range(m):
            if j == i:
                continue
            else:
                k += abs(x[j] - x1 + y[j] - y1)
        u.append(k)
    u.sort()
    print(u[0])