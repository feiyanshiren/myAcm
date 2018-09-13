n = int(input())
for i in range(n):
    s = input()
    s = s.replace("0", " ")
    ss = [int(j) for j in s.split()]
    if len(ss) == 0:
        print(0)
    else:
        ss.sort()
        r = ""
        for j in ss:
            r = r + str(j) + " "
        print(r.strip())
