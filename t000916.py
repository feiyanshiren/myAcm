try:
    while 1:
        n = int(input())
        d = [int(i) for i in input().split()]
        y = [int(i) for i in input().split()]
        d.sort(reverse=True)
        y.sort(reverse=True)
        r = ""
        for i in range(n):
            r = r + str(d[i]) + " "
            r = r + str(y[i]) + " "
        print(r.strip())
except Exception:
    pass
