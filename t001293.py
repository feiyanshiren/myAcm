try:
    while 1:
        s = input().split()
        if len(s) == 0:
            continue
        s1 = [int(i) for i in s]
        s2 = [int(i) for i in input().split()]
        m = {}
        if s1[2] >= 90:
            m["1"] = sum(s1)
        if s2[2] >= 90:
            m["2"] = sum(s2)
        r = sorted(m.items(), key=lambda x: x[1], reverse=True)
        ll = len(r)
        if ll == 0:
            print("-1")
        elif ll == 1:
            print(r[0][0])
        else:
            if r[0][1] == r[1][1]:
                print("1")
            else:
                print(r[0][0])
except EOFError:
    pass
