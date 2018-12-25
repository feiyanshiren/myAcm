try:
    while 1:
        n = int(input())
        k = 1
        a = 1
        while k:
            k = 10 * k + 1
            k = k % n
            a += 1
        print(a)
except: pass