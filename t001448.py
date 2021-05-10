try:
    f = 0
    while 1:
        n = int(input())
        if f:
            print()
        f = 1
        for i in range(n - 1):
            for j in range(i):
                print(" ", end="")
            for j in range(n - i):
                print("*", end="")
            for j in range(n - 2 - i):
                print(" ", end="")
            for j in range(i + 1):
                print("*", end="")
            print()
        for i in range(2 * n - 1):
            print("*", end="")
        print()
        for i in range(n - 1):
            for j in range(n - 1 - i):
                print("*", end="")
            for j in range(i):
                print(" ", end="")
            for j in range(i + 2):
                print("*", end="")
            for j in range(n - 2 - i):
                print(" ", end="")
            print()
except:
    pass
