try:
    while 1:
        s1 = [int(i) for i in input().split()]
        if len(s1) == 0:
            continue
        s2 = [int(i) for i in input().split()]
        z1 = sum(s1)
        z2 = sum(s2)
        r = -1
        if z1 >= z2:
            if s1[2] >= 90:
                r = 1
            else:
                if s2[2] >= 90:
                    r = 2
                else:
                    r = -1
        else:
            if s2[2] >= 90:
                r = 2
            else:
                if s1[2] >= 90:
                    r = 1
                else:
                    r = -1
        print(r)
except EOFError:
    pass
