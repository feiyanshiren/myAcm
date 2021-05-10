for T in range(int(input())):
    a = [int(i) for i in input().split()]
    y = 0
    y += min(a[0], a[4])
    y += min(a[1], a[5])
    y += min(a[2], a[3])
    print(y)
