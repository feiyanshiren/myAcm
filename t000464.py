try:
    while 1:
        c = int(input())
        a = [int(i) for i in input().split()]
        b = sum(a)
        n = 0
        for i in range(c):
            if (b - a[i]) % 2 == 0: n += 1
        print(n)
except Exception: pass
