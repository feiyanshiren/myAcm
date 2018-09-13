while 1:
    s = input()
    if s == "0.00":
        break
    n = float(s)
    d = 1
    while n > 0:
        n = n - 1 / (d + 1)
        d = d + 1
    print("%d card(s)" % (d - 1))
