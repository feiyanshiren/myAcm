for t in range(int(input())):
    s = input().split()
    z = 0
    for i in range(len(s[1])):
        z = int(s[1][i]) - 48 + z * 10
        z = z % 11
    if int(s[0]) == int(s[1]) and z == 0: print("YES")
    else: print("NO")
    