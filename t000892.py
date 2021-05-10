for t in range(int(input())):
    z = 0
    for n in range(int(input())):
        s = input().split()
        if float(s[1]) >= 1.5 and float(s[1]) <= 5 and int(s[2]) <= 300:
            z += float(s[1])
            print(s[0])
    if z == 0: print(-1)
    else: print("%.1f" % z)