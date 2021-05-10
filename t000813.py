while 1:
    s = [int(i) for i in input().split()]
    if s[0] == 0 and s[1] == 0:
        break
    b = int(s[0] / 2) + 1
    t = 0
    for i in range(1, b):
        if s[1] == (i * (s[0] - i)):
            t = 1
            break
    if t == 1:
        print("YES")
    else:
        print("NO")
