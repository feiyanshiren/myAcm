try:
    while 1:
        n = [int(i) for i in input().split()]
        v = 0
        for i in range(n[0], n[1] + 1):
            stri = str(i)
            if "7" not in stri:
                if i % 7 != 0:
                    z = 0
                    for j in stri:
                        z += int(j)
                    if z % 7 != 0:
                        v += i ** 2
        print(v)
except:
    pass