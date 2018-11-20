for T in range(int(input())):
     s = [float(i) for i in input().split()]
     x = s[0] * s[3] - s[1] * s[2]
     y = s[1] * s[3] - s[0] * s[2]
     print("%.2lf %.2lf" % (x, y))