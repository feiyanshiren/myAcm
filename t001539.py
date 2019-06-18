try:
    while 1:
        s = input().strip()
        y = int(input()) % len(s)
        print(s[y:] + s[:y])
except:
    pass