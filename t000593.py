try:
    while True:
        n = int(input())
        ss = input().split()
        if n == 0:
            print(0)
            continue
        t = 0
        for s in ss:
            if s == "1":
                n = n + 1
            else:
                n = n - 1
            t = t + 1
            if n == 0:
                break
        print(t)
except EOFError:
    pass
