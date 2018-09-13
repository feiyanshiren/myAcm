a = 0
while 1:
    n = int(input())
    if n == 0: break
    a += 1
    s = {}
    for i in range(n):
        s[i] = input()
    k = sorted(s.items(),  key=lambda d: len(d[1]))
    print("SET %d" % a)
    for i in range(0, n, 2):
        print(k[i][1])
    if n % 2 == 0:
        for i in range(n - 1, 0, -2):
            print(k[i][1])
    else:
        for i in range(n - 2, 0, -2):
            print(k[i][1])
