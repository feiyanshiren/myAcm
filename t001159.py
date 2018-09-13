t = int(input())
for i in range(t):
    o = []
    s = input()
    r = ""
    n = 0
    for j in s:
        if j == "O":
            o.append(j)
            ll = len(o)
            r = r + str(ll) + "+"
            n = n + ll
        else:
            o.clear()
            r = r + "0" + "+"
    r = r[: -1]
    print(r + "=" + str(n))
