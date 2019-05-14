m = []
v = []
for n in range(int(input())):
    s = input().split()
    m.append(s[0])
    m.append(s[1])
    v.append(s[2])
    v.append(s[2])
for k in range(int(input())):
    s = input().split()
    a = ""
    b = ""
    for i in range(len(m)):
        if s[0] == m[i]:
            a = v[i]
            break
    for i in range(len(m)):
        if s[1] == m[i]:
            b = v[i]
            break
    if a != b:
        print("Y")
    else:
        print("n")

    