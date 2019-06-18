try:
    while 1:
        s = list(input().strip())
        l = len(s)
        y = int(input()) % l
        for i in range(y, l):
            print(s[i], end="")
        for i in range(y):
            print(s[i], end="")
        print()
except:
    pass