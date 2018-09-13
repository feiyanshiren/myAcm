for n in range(int(input())):
    m = int(input())
    l1 = []
    l2 = []
    l3 = []
    for a in range(m):
        s = [int(i) for i in input().split()]
        l1.append(s[0])
        l2.append(s[1])
        l3.append(s[2])
    mc = max(l1)
    l1i = []
    for a in range(m):
        if mc == l1[a]:
            l1i.append(a)
    l22 = []
    l33 = []
    for a in l1i:
        l22.append(l2[a])
        l33.append(l3[a])
    ml = min(l22)
    l2i = []
    for i in range(len(l22)):
        if ml == l22[i]:
            l2i.append(i)
    l333 = []
    for i in l2i:
        l333.append(l33[i])
    l333.sort(reverse=True)     
    print(l333[0])
