for T in range(int(input())):
    a = [int(i) for i in input().split()]
    print(abs(a[2] - a[0]) + abs(a[3] - a[1]))
