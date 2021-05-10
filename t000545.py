for n in range(int(input())):
    f=1
    m=int(input())
    s=[]
    for i in range(m):
        s.append([int(k) for k in input().split()])
    for i in range(m):
        if s[i][i]!=0:
            print(1)
            f=0
            break
    if f==0: continue
    for i in range(m):
        if f==0: break
        for j in range(m):
            if i!=j and s[i][j]<=0:
                f=0
                print(2)
                break
    if f==0: continue
    for i in range(m):
        if f==0: break
        for j in range(m):
            if (i!=j) and (s[i][j]!=s[j][i]):
                print(3)
                f=0
                break
    if f==0: continue
    for i in range(m):
        if f==0: break
        for j in range(m):
            if f==0: break
            for k in range(m):
                if (i!=j) and (i!=k) and (j!=k) and (s[i][j]+s[j][k]<s[i][k]):
                    print(4)
                    f=0
                    break
    if f==0: continue
    print(0)
    