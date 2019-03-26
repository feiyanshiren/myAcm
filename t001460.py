for t in range(int(input())):
    a = [int(i) for i in input().split()]
    l = a[0] * a[2]
    r = a[1] * a[3]
    if l > r:
        print("left")
    elif l < r:
        print("right")
    else:
        print("shit,55555")
