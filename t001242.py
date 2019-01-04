for K in range(int(input())):
    NM = [int(i) for i in input().split()]
    a = [0]
    for i in range(1, NM[0] + 1):
        x = int(input())
        a.append(a[i - 1] + x)
    s = 0
    for i in range(1, NM[0] + 1):
        for j in range(i + NM[1] - 1, NM[0] + 1):
            t = (a[j] - a[i - 1]) * 1.0 / (j - i + 1)
            s = max(s, t)
    print(int(s * 1000))