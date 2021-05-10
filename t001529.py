try:
    while 1:
        n = int(input())
        s = []
        for i in range(n):
            s.append(input())
        t = []
        while len(s):
            d = s[::-1]
            if s < d:
                t.append(s.pop(0))
            else:
                t.append(s.pop())
        print("".join(t))
except:
    pass