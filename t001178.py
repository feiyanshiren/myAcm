import math


def ek(f1, f2):
    d = abs(f1 - f2)
    if d <= 0.00000001:
        return True
    else:
        return False


t = int(input())
for i in range(t):
    s = [float(j) for j in input().split()]
    if ek(s[4], 0):
        print("0.00")
    else:
        det = 4 * (s[0] - s[2]) ** 2 + 8 * (s[1] - s[3]) * s[4]
        a = s[1] - s[3]
        b = 2 * (s[0] - s[2])
        if det < 0:
            print("Drong is strong.")
        else:
            if ek(a, 0):
                if ek(b, 0):
                    print("Drong is strong.")
                else:
                    x = (2 * s[4]) / b
                    print("%.2f" % x)
            else:
                x1 = (-b + math.sqrt(det)) / (2 * a)
                x2 = (-b - math.sqrt(det)) / (2 * a)
                x = max(x1, x2)
                if x >= 0:
                    print("%.2f" % x)
                else:
                    print("Drong is strong.")
