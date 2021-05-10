for T in range(int(input())):
    s = [int(i) for i in input().split()]
    if s[0] > s[1]:
        s[0], s[1] = s[1], s[0]
    z = s[1] * (s[1] + 1) * (2 * s[1] + 1) // 6 -\
        s[0] * (s[0] + 1) * (2 * s[0] + 1) // 6 + s[0] * s[0] 
    print(z) 