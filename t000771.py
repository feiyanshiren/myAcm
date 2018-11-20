try:
    while 1:
        m = input()
        s = input()
        lm = len(m)
        a = ""
        for i in range(len(s)):
            t = int(m[i % lm]) + ord(s[i])
            if t > 122: t = t % 122 + 31
            a += chr(t)
        print(a)
except: pass