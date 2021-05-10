while 1:
    s = [i for i in input().split()]
    if s[0] == "0" and s[1] == "0":
        break
    else:
        j = 0
        w11 = int(s[0][2])
        w12 = int(s[0][1])
        w13 = int(s[0][0])
        w21 = int(s[1][2])
        w22 = int(s[1][1])
        w23 = int(s[1][0])
        if w11 + w21 > 9:
            j = j + 1
            w12 = w12 + 1
        if w12 + w22 > 9:
            j = j + 1
            w13 = w13 + 1
        if w13 + w23 > 9:
            j = j + 1
        print(j)
