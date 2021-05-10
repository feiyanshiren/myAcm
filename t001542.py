try:
    while 1:
        s = input()
        m = s
        for i in range(len(s)):
            t = s[:i] + s[i + 1:]
            if t < m:
                m = t
        print(m)
except:
    pass