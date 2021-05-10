try:
    while 1:
        s = input()
        if s[0].isalpha() or s[0] == "_":
            t = 1
            for i in s:
                if not i.isalpha() and i != "_"\
                   and not i.isdigit():
                    t = 0
                    break
            if t == 1:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
except Exception:
    pass
