for T in range(int(input())):
    s = input().split()
    if s[0] < s[1]: print(s[0] + ">" + s[1])
    elif s[0] == s[1]: print(s[0] + "=" + s[1])
    else: print(s[0] + "<" + s[1])
