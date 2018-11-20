try:
    while 1:
        n = int(input())
        s = [int(i) for i in input().split()]
        a = []
        t = 1
        for i in range(0, n ,3):
            if t == 1: a.append(max([s[i], s[i + 1], s[i + 2]]))
            else: a.append(min([s[i], s[i + 1], s[i + 2]]))
            t = -t
        print(max(a))
except: pass