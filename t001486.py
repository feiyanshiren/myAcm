try:
    while 1:
        n = [int(i) for i in input().split()]
        s = [i for i in range(3, 2 * n[0] + 2 , 2)]
        r = []
        j = 0
        z = 0
        for i in range(n[0]):
            z += s[i]
            j += 1
            if j == n[1]:
                r.append(str(z // j))
                j = 0
                z = 0
        if j != 0:
            r.append(str(z // j))
        print(" ".join(r))
except:
    pass