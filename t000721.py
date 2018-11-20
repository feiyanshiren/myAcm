m = {"J": "11", "Q": "12", "K": "13", "A": "1"}
for n in range(int(input())):
    s = input()
    y = input().split()
    y1 = y[0][:len(y[0]) - 1]
    y2 = y[0][len(y[0]) - 1:]
    z1 = y[1][:len(y[1]) - 1]
    z2 = y[1][len(y[1]) - 1:]
    y2 = 10 if y2 == s else 1
    z2 = 10 if z2 == s else 1
    y1 = m.get(y1, y1)
    z1 = m.get(z1, z1)
    s1 = int(y1) * int(y2)
    s2 = int(z1) * int(z2)
    if s1 > s2: print("YES")
    else: print("NO")