try:
    while 1:
        s = input()
        m = s[0]
        k = 0
        for i in range(len(s)):
            t = s[i]
            if t > m:
                m = t
                k = i
        print(s[: k] + s[k + 1 :])
except:
    pass