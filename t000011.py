t = int(input())
for i in range(t):
    n = int(input())
    d = ""
    o = ""
    for j in range(1, n + 1, 2):
        d = d + str(j) + " "
        o = o + str(j + 1) + " "
    print(d)
    print(o)
    print()
