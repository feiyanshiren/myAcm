try:
    while 1:
        s = [int(i) for i in input().split()][::-1]
        for i in s:
            print(i, end=" ")
        print()
except: pass