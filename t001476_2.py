try:
    while 1:
        for t in range(int(input())):
            N = int(input())
            for i in range(N, -1, -2):
                for j in range((N - i) // 2):
                    print(" ", end="")
                for j in range(i):
                    print("*", end="")
                print()
except:
    pass
