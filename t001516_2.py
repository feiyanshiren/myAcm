for T in range(int(input())):
    s = input().lower()
    l, w, p = 0, 0, 0
    for i in s:
        if i == "l":
            l += 1
        elif i == "w":
            w += 1
        elif i == "p":
            p += 1
    print(min(l, w, p))