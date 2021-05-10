t = 0
try:
    while True:
        s = input().split()
        t = t + (float(s[1]) * float(s[2]))
except EOFError:
    print("%.1f" % t)
