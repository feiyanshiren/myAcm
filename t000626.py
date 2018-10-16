try:
    while 1:
        input()
        j = 0
        m = [i for i in input().split()]
        n = {i: 0 for i in input().split()}
        for i in m:
            if n.get(i, -1) != -1:
                j += 1
        print(j)
except: pass