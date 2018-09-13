def q(n):
    d = ""
    for i in range(2, 10):
        if d != "": break
        for k in range(i, 10):
            if n == i * k:
                d = str(i) + str(k)
                break
    if d == "":
        for i in range(2, 10):
            if d != "": break
            for k in range(i, 10):
                if d != "": break
                for j in range(k, 10):
                    if n == i * k * j:
                        d = str(i) + str(k) + str(j)
                        break
    if d == "":
        for i in range(2, 10):
            if d != "": break
            for k in range(i, 10):
                if d != "": break
                for j in range(k, 10):
                    if d != "": break
                    for l in range(j, 10):
                        if n == i * k * j * l:
                            d = str(i) + str(k) + str(j) + str(l)
                            break
    if d == "": d = "-1"
    return d


try:
    while 1:
        n = int(input())
        if n == 0: print(10)
        elif n > 0 and n <= 9: print(n)
        else: print(q(n))
except Exception:
    pass
