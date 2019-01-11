try:
    while 1:
        n = int(input())
        s = [int(i) for i in input().split()]
        h = 0
        for i in range(n):
            a = s[i]
            if a >= 0:
                h += a
            else:
                h += a * (i + 1)
        print(h)
except:
    pass
