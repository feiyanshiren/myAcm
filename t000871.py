for T in range(int(input())):
    m = int(input())
    ma = {}
    for i in range(m):
        s = input()
        s1 = s.split()
        ma[s] = int(s1[2]) 
    d = sorted(ma.items(), key=lambda k: k[1], reverse=True)
    p = ""
    for i in d: p = p + i[0] + " "
    print(p)