while 1:
    N = int(input())
    if N == 0: break
    s = [int(i) for i in input().split()]
    s.sort()
    z = int(N / 2) + 1
    m = 0
    for i in range(z): m += int(s[i] / 2) + 1
    print(m)

