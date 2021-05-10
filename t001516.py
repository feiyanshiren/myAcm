for T in range(int(input())):
    s = input()
    l = 0
    w = 0
    p = 0
    for i in s:
        if i == "l" or i == "L":
            l += 1
        elif i == "w" or i == "W":
            w += 1
        elif i == "p" or i == "P":
            p += 1
    if l > 0 and w > 0 and p > 0:
        print(min(l, w, p))
    else:
        print(0)
            
        