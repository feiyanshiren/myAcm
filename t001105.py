try:
    while 1:
        n = int(input())
        a = []
        s = 0
        ff = 0
        s1 = 0
        a = [int(i) for i in input().split()]
        s = sum(a)
        if s % n:
            ff = -1
        ave = s // n
        for i in range(n):
            if a[i] > ave:
                if (a[i] - ave) % 2 != 0:
                    ff = -1
                    break
                else:
                    s1 += (a[i] - ave) // 2
            elif a[i] < ave:
                if (ave - a[i]) % 2:
                    ff = -1
                    break
        if ff:
            print(-1)
        else:
            print(s1)
except:
    pass
