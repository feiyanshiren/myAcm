try:
    while 1:
        s = [int(i) for i in input().split()]
        for i in range(s[0], s[1] + 1):
            if i % 3 == 0:
                print(i, end=" ")
        print()
except: pass