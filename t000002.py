n = int(input())
r = []
for i in range(n):
    s = input()
    z = []
    for s_i in s:
        if s_i == "(" or s_i == "[":
            z.append(s_i)
        elif s_i == ")":
            if len(z) != 0 and "(" == z[-1]:
                z.pop()
            else:
                z.append(s_i)
        elif s_i == "]":
            if len(z) != 0 and "[" == z[-1]:
                z.pop()
            else:
                z.append(s_i)
    if len(z) == 0:
        r.append("Yes")
    else:
        r.append("No")
for i in r:
    print(i)
