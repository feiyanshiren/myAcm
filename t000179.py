while 1:
    n = int(input())
    if n == 0:
        break
    a = [int(i) for i in input().split()]
    f = [int(i) for i in input().split()]
    a.sort()
    s = [0 for i in range(102)]
    j = 0
    p = 1
    for i in range(n - 1, -1, -1):
        if j == f[0]:
            p += 1
            j = 0
        j += 1
        s[i] = a[i] + p * f[1]
    s.sort()
    print(s[-1])
