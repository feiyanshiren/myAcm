for T in range(int(input())):
    e = bin(int(input())).replace("0b", "")
    ll = len(e)
    f = ll - e.rfind("1")
    c = e.count("1")
    print("%d %d %d %d" % (f, 32 - ll, f - 1, c))