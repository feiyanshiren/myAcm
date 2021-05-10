for N in range(int(input())):
    a = input()
    b = input()
    c = 0
    d = b.find(a)
    while d != -1:
        c += 1
        d = b.find(a, d + 1)
    print(c)
