for N in range(int(input())):
    s = input()
    d = [""]
    for i in range(len(s)):
        d[len(d) - 1] = d[len(d) - 1] + s[i]
        if d[len(d) - 1][:: -1] not in s:
            d[len(d) - 1] = d[len(d) - 1][: len(d[len(d) - 1]) - 1]
            d.append(s[i])
    f = sorted(d, key=lambda x: len(x), reverse=True)
    print(f[0])
    