try:
    while 1:
        n = 0
        s = [int(i) for i in input().split()]
        for i in s:
            if i % 2 != 0: n += 1
        print(n)
except: pass