try:
    while 1:
        s = input()
        if s == "0 0":
            break
        s = [int(i) for i in s.split()]
        if s[0] == s[1]:
            print(0)
        else:
            n1 = s[1]
            n2 = s[0]
            c = 0
            if s[1] - s[0] > 1:
                while s[0]:
                    c = s[1] % s[0]
                    s[1] = s[0]
                    s[0] = c
            if s[1] == 1:
                print(n1 - n2 + 1)
            else:
                print(n1 - n2)
except:
    pass