for n in range(int(input())):
    l = []
    for m in range(int(input())):
        s = [int(i) for i in input().split()]
        if s[1] < s[2]:
            s[1], s[2] = s[2], s[1]
        l.append(s)
    l.sort(key=lambda x: (x[0], x[1], x[2]))
    a = {}
    for i in l:
        b = ""
        for j in i:
            b += str(j) + " "
        a[b.strip()] = ""
    for i in a.keys():
        print(i)
