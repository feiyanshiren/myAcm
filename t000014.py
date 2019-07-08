for m in range(int(input())):
    n = int(input())
    a = []
    for i in range(n):
        s = [int(j) for j in input().split()]
        a.append(s)
    a.sort(key=lambda x: x[1])
    h = 1
    b = [a[0]]
    for i in a:
        if i[0] > b[-1][1]:
            b.append(i)
            h += 1
    print(b)
    print(h)