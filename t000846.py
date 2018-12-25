for T in range(int(input())):
    s = [int(i) for i in input().split()]
    c = 0
    a = 0
    while c != s[2]:
        c = int((s[0] + s[1]) / 2)
        a += 1
        if c < s[2]: s[0] = c + 1
        else: s[1] = c
    if a % 2: print("Win")
    else: print("Lose")