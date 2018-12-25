try:
    while 1:
        s = input()
        a = ""
        c = 0
        ll = len(s)
        for i in s:
            a += i
            l2 = len(a)
            if ll % l2:
                continue
            else:
                b = ""
                for j in range(ll // l2):
                    b += a
                if b == s:
                    break
                else:
                    continue
        print(len(a))
except:
    pass