for t in range(int(input())):
    s = input()
    mx = 0
    d = ""
    for i in s:
        m = s.count(i)
        if m > mx:
            mx = m
            d = i
        elif m == mx:
            if d > i:
                d = i
    print(d)
