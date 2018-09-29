for N in range(int(input())):
    s = list(input())
    for i in range(0, len(s), 2):
        if s[i].islower(): s[i] = s[i].upper()
    print("".join(s))
