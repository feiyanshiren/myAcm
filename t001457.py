for T in range(int(input())):
    a = [int(i) for i in input().split()]
    if a[0] > 0 and a[1] > 0 and a[2] > 0:
        if a[0] + a[1] > a[2] and a[0] + a[2] > a[1] and a[1] + a[2] > a[0]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")