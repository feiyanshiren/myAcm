for T in range(int(input())):
    s = [int(i) for i in input().split()]
    if (s[0] - s[1]) % 3 and (s[1] - s[2]) % 3 and (s[0] - s[2]) % 3: print("NO")
    else: print("YES")