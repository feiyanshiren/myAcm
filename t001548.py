try:
    while 1:
        s = [i for i in input().split()]
        y = 0
        for i in range(int(s[1])):
            y += int(s[0] * (i + 1))
        print(y)
except:
    pass
