for T in range(int(input())):
    n = int(input())
    for i in range(n):
        for j in range(n - i):
            print(" ", end="")
        print("*")
    for i in range(n):
        print("*", end="")
    print("*")
    for i in range(n):
        for j in range(n - i - 1):
            print(" ", end="")
        print("*")
    print()
        