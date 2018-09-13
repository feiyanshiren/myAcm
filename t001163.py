try:
    while 1:
        input()
        nm = {i: int(j) for i, j in enumerate(input().split())}
        f = sorted(nm.items(), key=lambda d: d[1])
        s = ""
        for i in f:
            s = s + str(i[0]) + " "
        print(s.strip())
except EOFError:
    pass
