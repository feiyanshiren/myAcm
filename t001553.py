for T in range(int(input())):
    n = [int(i) for i in input().split()]
    k = []
    for i in range(n[0]):
        s = [int(j) for j in input().split()]
        k.append(s)
    for i in range(n[1]):
        for j in range(n[0]):
            if j < n[0] - 1:
                print(k[j][i], end=" ")
            else:
                print(k[j][i])
    print()
