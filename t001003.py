try:
    while 1:
        n = int(input())
        if n == 0:
            print(1)
            continue
        k = 4 * n * n - 4 * n + 2
        print(k)
except Exception:
    pass
