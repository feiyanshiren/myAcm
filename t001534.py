try:
    while 1:
        a = input().split()
        l1 = len(a[0])
        l2 = len(a[1])
        mi = l1 if l1 < l2 else l2
        ll1 = list(a[0])[::-1]
        ll2 = list(a[1])[::-1]
        b = ll1 if l1 > l2 else ll2
        for i in range(mi):
            c = int(ll1[i]) + int(ll2[i])
            b[i] = str(c)[-1]
        print(int("".join(b[::-1])))
except:
    pass