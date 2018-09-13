t = int(input())
for i in range(t):
    n = int(input())
    hs = [int(k) for k in input().split()]
    if n <= 0:
        print("%d" % n)
        continue
    elif n == 1:
        print("%d" % n)
        continue
    elif n == 2:
        print("%d" % n)
        continue
    else:
        cnt = 2
        for k in range(1, n - 1):
            hsz = hs[:k]
            hsy = hs[(k + 1):]
            hsz.sort()
            hsy.sort()
            if hs[k] >= hsz[-1] or hs[k] >= hsy[-1]:
                cnt = cnt + 1
        print("%d" % cnt)
