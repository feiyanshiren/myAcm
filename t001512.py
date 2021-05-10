try:
    while 1:
        n = int(input())
        if n <= 0:
            print(0)
            continue
        s = [int(i) for i in input().split()]
        n = len(s)
        h = 0
        for i in range(n):
            if s[i] >= 0:
                h += s[i]
            else:
                h += s[i] * (i + 1)
        print(h)
except:
    pass
