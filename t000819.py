try:
    while 1:
        s = input()
        cs = s.count("c")
        ll = len(s)
        if cs == 0: print(ll - 1)
        elif cs % 2 != 0: print(0)
        elif cs % 2 == 0:
            k = int(cs / 2)
            id = 0
            for i in range(ll):
                if s[i] == "c": k -= 1
                if k == 0:
                    id = i
                    break
            s = s[(id + 1):]
            s = s.partition("c")[0]
            print(len(s) + 1)
except: pass