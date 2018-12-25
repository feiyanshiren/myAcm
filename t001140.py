for T in range(int(input())):
    a = []
    for N in range(int(input())):
        s = input().split()
        if s[0] == "push":
            a.append(s[1])
        else:
            if len(a):
                a.pop()
    if len(a):
        a.reverse()
        print(" ".join(a))
    else:
        print("no eggs!")