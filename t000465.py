for N in range(int(input())):
    M = [i for i in input()]
    M.sort(reverse=True)
    d = "".join(M)
    M.sort()
    x = "".join(M)
    print("%d %d"%(int(d),int(x)))