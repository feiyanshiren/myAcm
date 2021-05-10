for N in range(int(input())):
    s = [int(i) for i in input().split()]
    d = {}
    for i in range(s[0], s[1] + 1):
        d[i] = int(str(i)[::-1])
    f = sorted(d.items(), key=lambda x: x[1])
    for i in f:
        print(i[0], end=" ")
    print()
