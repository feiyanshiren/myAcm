while 1:
    n = int(input())
    if n == 0:
        break
    s = [int(i) for i in input().split()]
    su = sum(s)
    pj = su / n
    w = 1000
    z = 0
    for i in range(n):
        a = abs(pj - s[i])
        if a <= w:
            w = a
            z = i
    d = s.pop(z)
    j = 0
    for i in s:
        j = j + abs(i - d)
    print(j)
