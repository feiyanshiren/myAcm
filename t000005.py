for N in range(int(input())):
    a = input()
    b = input()
    c = 0
    d = b.find(a)
    while d != -1:
        c += 1
        b = b[d + 1:]
        d = b.find(a)
    print(c)
