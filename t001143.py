try:
    while 1:
        n = int(input())
        if n == 1:
            print(1)
            continue
        a = [[0 for i in range(n)] for i in range(n)]
        b = 1
        for i in range(n):
            for j in range(n - i):
                a[i][j + i] = b
                b += 1
            for j in range(n - i - 1):
                a[j + i + 1][i] = b
                b += 1
        for i in range(n):
            print(" ".join([str(j) for j in a[i]]))
except:
    pass
