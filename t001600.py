for T in range(int(input())):
    n = [int(i) for i in input().split()]

    a = [[0 for j in range(n[1])] for i in range(n[0])]

    l = 0

    for i in range(n[0]):
        for j in range(i + 1):
            if j < n[1]:
                a[i - j][j] = l
                l += 1

    """
    for i in range(n[1] - 2, -1, -1):
        for j in range(i + 1):
            a[n[0] - j - 1][n[1] - i + j - 1] = l
            l += 1
    """
    for i in a:
        for j in i:
            print(j, end=" ")
        print()
    print()
