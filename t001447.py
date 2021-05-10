try:
    while 1:
        input()
        s = [int(i) for i in input().split()]
        s.sort()
        for i in s:
            print(i, end=" ")
        print()
except:
    pass
