for T in range(int(input())):
    n = int(input())
    k = 2 * n - 1
    z = k // 2
    for i in range(z):
        a = z - i
        for j in range(a):
            print(" ", end="")
        for j in range(2 * i + 1):
            print("*", end="")
        for j in range(a):
            print(" ", end="")
        print()
    for i in range(2 * n - 1):
        print("*", end="")
    print()
    for i in range(z + 1, k):
        a = i - z
        for j in range(a):
            print(" ", end="")
        for j in range(2 * (k - i) - 1):
            print("*", end="")
        for j in range(a):
            print(" ", end="")
        print()