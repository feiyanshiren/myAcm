for T in range(int(input())):
    s = [float(i) for i in input().split()]
    if abs((s[0] + s[1]) - s[2]) < 0.0001: print("Yes")
    else: print("No")