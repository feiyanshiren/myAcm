def q(n, m, nm, mm, li):
    i = 1
    while i * n <= nm:
        j = 1
        while j * m <= mm:
            li[i * n - 1][j * m - 1] = - li[i * n - 1][j * m - 1]
            j += 1
        i += 1
    

for T in range(int(input())):
    n = [int(i) for i in input().split()]
    li = [[1 for i in range(n[1])] for j in range(n[0])]
    for i in range(n[0]):
        for j in range(n[1]):
            q(i + 1, j + 1, n[0], n[1], li)
    f = 0
    for i in range(n[0]):
        for j in range(n[1]):
            if li[i][j] == -1:
                f += 1
    print(f)
