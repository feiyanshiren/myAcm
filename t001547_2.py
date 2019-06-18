for T in range(int(input())):
    s = input().strip()
    a = 0
    b = 0
    for i in s:
        if i == "0":
            a += 1
        else:
            b += 1
    print("%d %d" % (a, b))