def ifK(kgs, b, i):
    kg = kgs[i]
    ll = len(kgs)
    if kg[0] >= b:
        return True
    else:
        zl = 0
        yl = 0
        d = 1
        while 1:
            c = i - d
            if c >= 0:
                kgz = kgs[c]
                if kgz[1] <= kg[1]:
                    zl = zl + kgz[0]
                    d = d + 1
                else:
                    break
            else:
                break
        d = 1
        while 1:
            c = i + d
            if c < ll:
                kgy = kgs[c]
                if kgy[1] <= kg[1]:
                    yl = yl + kgy[0]
                    d = d + 1
                else:
                    break
            else:
                break
        if zl + yl + kg[0] >= b:
            return True
        else:
            return False


for n in range(int(input())):
    m = int(input())
    kgs = []
    for i in range(m):
        kgs.append([int(j) for j in input().split()])
    b = int(input())
    ks = []
    for i in range(m):
        if ifK(kgs, b, i):
            ks.append(kgs[i][1])
    ks.sort()
    if len(ks) == 0:
        print()
    else:
        print(ks[0] + b)
