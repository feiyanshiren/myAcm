try:
    while 1:
        n = [int(i) for i in input().split()]
        for i in range(n[0]):
            if i == 0 or i == n[0] - 1 or i == n[0] // 2:
                print("*" * n[1])
            else:
                k = (n[1] // 2 - 1)
                print("*" + " " * k + "*" + " " * k + "*")
        print()
except:
    pass
