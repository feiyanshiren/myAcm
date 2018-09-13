while 1:
    s = input().split()
    if s[0] == "0" and s[1] == "0":
        break
    t = ""
    for i in range(10):
        for k in range(10):
            ns = str(i) + str(k)
            dd = s[0] + ns
            if int(dd) % int(s[1]) == 0:
                t = t + ns + " "
    print(t.strip())
