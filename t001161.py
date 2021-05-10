try:
    while 1:
        n = int(input())
        c = 0
        while n != 1:
            if n % 2 == 0:
                n = n / 2
            else:
                n = 3 * n + 1
            c = c + 1
        print(c % 3)
except EOFError:
    pass
