
a = []
while True:
    n = int(input())
    if n < 56 and n > 0:
        if n == 1:
            a.append(1)
        else:
            m0 = 1
            m1 = 0
            m2 = 0
            m3 = 0
            for i in range(1, n):
                m0 = m0 + m3
                m3 = m2
                m2 = m1
                m1 = m0
            a.append(m0 + m1 + m2 + m3)
    else:
        break
for i in a:
    print(i)
