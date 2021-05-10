for N in range(int(input())):
    s = [i for i in input()]
    if s[0] > s[1]:
        s[0], s[1] = s[1], s[0]
    if s[1] > s[2]:
        s[1], s[2] = s[2], s[1]
    if s[0] > s[1]:
        s[0], s[1] = s[1], s[0]
    print(" ".join(s))