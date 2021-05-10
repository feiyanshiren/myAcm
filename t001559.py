for T in range(int(input())):
    s = input().rstrip()
    a = []
    for i in s:
        if i.isdecimal():
            a.append(i)
    a.sort(reverse=True)
    d = "".join(a)
    if d == "":
        d = "0"
    if int(d) < 1000:
        print("No")
    else:
        print("Yes")
