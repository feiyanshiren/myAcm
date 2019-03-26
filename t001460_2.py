for t in range(int(input())):
    a = [int(i) for i in input().split()]
    l = a[0] * a[2] - a[1] * a[3]
    if l > 0:
        print("left")
    elif l < 0:
        print("right")
    else:
        print("shit,55555")
