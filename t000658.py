try:
    while 1:
        s = input().split()
        a = list(s[0])
        for i in range(int(s[1])):
            b = a.pop()
            a.insert(0, b)
        print("".join(a))
except: pass