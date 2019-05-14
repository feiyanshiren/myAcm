try:
    while 1:
        a = [list(i)[::-1] for i in input().split()]
        b = a[0] if len(a[0]) > len(a[1]) else a[1]
        for i in range(min(len(a[0]), len(a[1]))):
            b[i] = str(int(a[0][i]) + int(a[1][i]))[-1]
        print(int("".join(b[::-1])))
except:
    pass