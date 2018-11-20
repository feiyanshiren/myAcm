try:
    while 1:
        input()
        s = [bin(int(i)) for i in input().split()]
        b = []
        for i in s:
            if i.count("1") % 2 == 0: b.append(int(i, 2))
        print(bin(sum(b))[2:])
except: pass