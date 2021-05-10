try:
    while 1:
        n = int(input())
        m = 2 * n + 1
        s = " " * ((n + 1) // 2) + "*" * n
        for i in range(n):
            print(s)
        z = n - 4
        c = (m - z) // 2
        d = n // 2
        s = " " * c + "*" * z
        for i in range(d):
            print(s)
        print("*" * m)
        for i in range(d):
            print(s)
        print()
except:
    pass