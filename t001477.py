for T in range(int(input())):
    s1 = list(input())
    s2 = list(input())
    m1 = {}
    m2 = {}
    for s in s1:
        m1[s] = m1.get(s, 0) + 1
    for s in s2:
        m2[s] = m2.get(s, 0) + 1
    e1 = sorted(m1.items(), key=lambda d: d[1], reverse=True)
    e2 = sorted(m2.items(), key=lambda d: d[1], reverse=True)
    n1 = []
    n2 = []
    e11 = e1[0][1]
    e21 = e2[0][1]
    for e in e1:
        if e11 == e[1]:
            n1.append(e[0])
    for e in e2:
        if e21 == e[1]:
            n2.append(e[0])
    n1.sort()
    n2.sort()
    if n1[0] == n2[0]:
        print("YES")
    else:
        print("NO")