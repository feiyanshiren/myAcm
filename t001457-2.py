for T in range(int(input())):
    a = [int(i) for i in input().split()]
    a.sort()
    if a[0] > 0 and a[1] > 0 and a[2] > 0:
        if a[0] + a[1] > a[2]:
            print("YES")
        else:
            print("NO")
    else:
        print("NO")