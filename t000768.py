def to_move(s, k):
    aa = ord(s)
    for i in range(k):
        aa = aa - 1
        if aa < 65:
            aa = 90
    return chr(aa)


try:
    while 1:
        s = input().split()
        ss = ""
        for i in s[0]:
            d = to_move(i, int(s[1]))
            ss = ss + d
        print(ss)
except Exception:
    pass
