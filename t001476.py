try:
    while 1:
        for t in range(int(input())):
            N = int(input())
            for i in range(N, -1, -2):
                print(" " * ((N - i) // 2) + "*" * i)
except:
    pass
