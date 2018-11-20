try:
    while 1:
        s = input().split()
        x = int(s[1])
        i = 1
        while 1:
            if (26 * i + 1) % x == 0: break
            i += 1
        x =int((26 * i + 1) / x)
        for i in s[0]: print("%c" %(x * (ord(i) - 65) % 26 + ord("A")), end="")
        print()
except: pass