try:
    while 1:
        s = input()
        if s == "": continue
        n = [int(i) for i in s.split()]
        m = [int(i) for i in input().split()]
        m.sort()
        i = 0
        for j in m:
            n[1] -= j
            if n[1] < 0: break
            i += 1
        print(i)
except: pass