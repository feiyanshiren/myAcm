try:
    n = 0
    while 1:
        s = input().split("=")
        if str(eval(s[0])) == s[1]: n += 1
except: print(n)