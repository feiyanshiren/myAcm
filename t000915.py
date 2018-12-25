try:
    while 1:
        s = [i for i in input().strip()]
        t = [i for i in input().strip()]
        if s.count("+") != t.count("+"):
            print("-1")
            continue
        n = 0
        c = len(s)
        for i in range(c):
            if s[i] != t[i]:
                for j in range(i + 1, c):
                    if s[j] == t[i]:
                        break
                n = n + (j - i)
                s[j] = s[i]
        print(n)
except: pass