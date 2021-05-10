def t1131(n, m):
    cnm = 1
    if m > n - m:
        m = n - m
    if m <= 0 or n <= 0:
        return 1
    fz = n
    fm = m
    while m > 1:
        fz = fz * (n - 1)
        fm = fm * (m - 1)
        n = n - 1
        m = m - 1
    cnm = fz / fm
    return int(cnm)


t = int(input())
for i in range(t):
    nm = [int(j) for j in input().split()]
    print(t1131(nm[0], nm[1]))
