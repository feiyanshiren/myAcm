for T in range(int(input())):
    n = int(input())
    a = 2 * n - 1
    for i in range(a, -1, -2):
        k = a - i
        if k > 0:
            for j in range(k // 2):
                print(" ", end="")
        for j in range(i):
            print("*", end="")
        print()
    for i in range(3, a + 2, 2):
        k = a - i
        if k > 0:
            for j in range(k // 2):
                print(" ", end="")
        for j in range(i):
            print("*", end="")
        print()
    print()
        