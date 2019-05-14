# 未完
for T in range(int(input())):
    s = [int(i) for i in input().split()]
    m = []
    for i in range(s[0]):
        m1 = []
        for j in range(s[0]):
            m1.append("-")
        m.append(m1)
    for i in range(s[1]):
        a = [int(j) for j in input().split()]
        