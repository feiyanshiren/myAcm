try:
    while 1:
        n = [int(i) for i in input().split()]
        f = False
        for i in range(10, 101):
            if i % 3 == n[0] and i % 5 == n[1] and i % 7 == n[2]:
                print(i)
                f = True
                break
        if not f:
            print("No answer")
except EOFError:
    pass
