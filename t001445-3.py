try:
    while 1:
        n = int(input())
        a = 1
        for i in range(1, n + 1):
            a *= i
        print(a)
except:
    pass