try:
    m = []
    s = list("0123456789abcdefghiklmnopqrst")
    v = list("edfgcbhia9kl87mn65op43qr21st0")
    for i in range(29):
        for j in range(29):
            if s[i] == v[j]:
                m.append(j)
                break
    while 1:
        s = list(input())
        for i in range(29):
            b = m[i]
            v[i] = s[b]
        print("".join(v))
except:
    pass