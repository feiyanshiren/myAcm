try:
    while 1:
        m = {}
        n = []
        input()
        b = [int(i) for i in input().split()]
        c = [int(i) for i in input().split()]
        b.sort(reverse=True)
        for i in b: m[i] = m.get(i, 0) + 1
        for i in b:
            n.append(m.get(i, 0))
            if i in m.keys(): del m[i]
        for i in c: print(n[i - 1])
except: pass