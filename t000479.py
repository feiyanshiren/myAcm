try:
    while 1:
        s = int(input())
        t = s
        for i in range(2, s + 1):
            if s % i == 0:
                t = int(t / i * (i - 1))
            while s % i == 0:
                s = int(s / i)
        print(t)
except: pass