try:
    while 1:
        s = input().strip()
        s = s.replace("/", "//")
        s = s.replace("^", "**")
        print(eval(s))
except:
    pass