for n in range(int(input())):
    l = []
    for m in range(int(input())):
        s = [int(i) for i in input().split()]
        if s[1] < s[2]:
            s[1], s[2] = s[2], s[1]
        l.append(s)
    l.sort(key=lambda x: (x[0], x[1], x[2]))
    k = []
    [k.append(i) for i in l if not i in k]
    [print(" ".join([str(j) for j in i])) for i in k]
