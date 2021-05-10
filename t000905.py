for T in range(int(input())):
    s = input()
    n = []
    n.append(s[0])
    for i in range(1, len(s)):
        if n[0] >= s[i] and s[i] != "0": n.insert(0, s[i])
        else: n.append(s[i])
    print("".join(n))
        