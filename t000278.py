for n in range(int(input())):
    m = [int(i) for i in input().split()]
    k = [i for i in range(1, m[0] + 1)]
    while len(k) != 1:
        d = m[1] - 1
        d = d % len(k)
        del k[d]
        k = k[d:] + k[0: d]
    print(k[0])
