while True:
    n = int(input())
    if n == 0:
        break
    tt = []
    for i in range(n):
        s = input().split()
        t = int(s[0]) + int(s[1])
        tt.append(t)
    tt.sort()
    print(tt[-1])
