try:
    while 1:
        s = [int(i) for i in input().split()]
        d = 0
        for i in range(1, s[1] + 1):
            d = d + 1
            if d % 5 == 0:
                s[0] = s[0] + 6
                d = 1
            else:
                s[0] = s[0] + 1
        print(s[0])
except EOFError:
    pass
