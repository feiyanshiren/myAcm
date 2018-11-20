try:
    c = "CAmEm"
    while 1:
        s = input()
        j = 0
        b = 1
        for i in range(len(s)):
            if j == 5: j =0
            if s[i] != c[j]:
                b = 0
                break
            j += 1
        if b: print("YES")
        else: print("NO")
except: pass