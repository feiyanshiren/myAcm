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
    u = 0
    for i in range(m // 2):
        u += x[m - 1 - i] - x[i] + y[m - 1 - i] - y[i]
    print(u)