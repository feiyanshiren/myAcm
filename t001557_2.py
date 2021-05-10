for T in range(int(input())):
    a = [int(i) for i in input().split()]
    print(max(a[2], a[0]) - min(a[2], a[0]) + max(a[3], a[1]) - min(a[3], a[1]))
