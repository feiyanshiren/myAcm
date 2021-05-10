try:
    while 1:
        n = int(input())
        s = sum([int(i) for i in input().split()])
        if s % n == 0:
            print(n)
        else:
            print(n - 1)
except EOFError:
    pass
