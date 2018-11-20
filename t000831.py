try:
    while 1:
        n = int(input())
        m = sum([int(i) for i in input().split()])
        print(m + n + int(n / 5) * 5)
except: pass