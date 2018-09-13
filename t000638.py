try:
    while True:
        ss = sum([5 + int(s) * 10 for s in input().split()])
        kk = sum([int(s) for s in input().split()])
        tt = kk - ss
        if tt <= 0:
            print("No !")
        else:
            print("Yes %d" % tt)
except EOFError:
    pass
