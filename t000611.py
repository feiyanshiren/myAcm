try:
    while True:
        n = int(input())
        if n % 2 != 0:
            n = n - 1
        print(int((n * n + 2 * n) / 4))
except EOFError:
    pass
