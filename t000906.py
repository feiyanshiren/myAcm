def YangHui (num):
    LL = [[1]]
    for i in range(1,num):
        LL.append([(0 if j== 0 else LL[i-1][j-1])+ (0 if j ==len(LL[i-1]) else LL[i-1][j]) for j in range(i+1)])
    return LL

try:
    while 1:
        c = int(input())
        l = YangHui(c)
        s = ""
        for i in l:
            for k in i:
                s += str(k)
                s += " "
            s += "\n"
        print(s)
except: pass
