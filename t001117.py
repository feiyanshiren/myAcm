for T in range(int(input())):
    a = []
    for N in range(int(input())):
        s = input().split()
        if s[0] == "push":
            a.append(s[1])
        else:
            a.pop(0)
    if len(a):
        print(" ".join(a))
    else: 
        print("no eggs!")