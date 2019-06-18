try:
    while 1:
        n = int(input())
        k =  (n + 1) // 2
        m = 2 * n + 1
        for i in range(n):
            print(" " * k, end="")
            print("*" * n)
        z = n - 4
        c = (m - z) // 2
        d = n // 2
        for i in range(d):
            print(" " * c, end="")
            print("*" * z)
        print("*" * m)
        for i in range(d):
            print(" " * c, end="")
            print("*" * z)
        print()
except:
    pass