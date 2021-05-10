try:
    while 1:
        n = [int(i) for i in input().split()]
        a = [[] for i in range(n[1])]
        for i in range(n[0]):
            s = input().split()
            m = 0
            k = s[0]
            for l in range(len(s)):
                j = s[l]
                q = s.count(j)
                if q > m:
                    m = q
                    k = j
                a[l].append(j)
            print(k)
        for i in a:
            m = 0
            k = i[0]
            for j in i:
                q = i.count(j)
                if q > m:
                    m = q
                    k = j
            print(k)
except:
    pass