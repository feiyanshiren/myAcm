try:
    while 1:
        s = input()
        m = {}
        for i in s:
            m[i] = m.get(i, 0) + ord(i)
        d = sorted(m.items(), key=lambda x: x[1])
        print(d[-1][1])
except:
    pass
