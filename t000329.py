for t in range(int(input())):
    s = input().split(".")
    d = ""
    if len(s) < 2: print("-1 1")
    else:
        l = len(s[1])
        for i in s[1]:
            d = d + i
            ll = len(d)
            k = ""
            for j in range(int(l / ll)): k = k + d
            if k == s[1]: break
        print("%d %s %d" % (len(d), d, s[1].count(d)))
        