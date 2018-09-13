try:
    while True:
        n = int(input())
        t = 0
        if n == 0:
            t = 1
        elif n > 0:
            t = int((n * (n + 1)) / 2)
        else:
            n = n * -1
            t = int((n * (n + 1)) / 2)
            t = (t * -1) + 1
        print(t)
except EOFError:
    pass
