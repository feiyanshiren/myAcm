def f(n):
    d = ""
    for i in range(1,n+1):
        for j in range(i,10):
            d+="%d*%d=%d "%(i,j,i*j)
        d = d.strip()
        d += "\n"
    return d
for N in range(int(input())):
    M = int(input())
    print(f(M))