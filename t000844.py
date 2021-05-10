while 1:
    s = input().split()
    if s[0] == "0" and s[1] == "0": break
    print(int(s[0][::-1]) + int(s[1][::-1]))