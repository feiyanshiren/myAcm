def f(x):
    s = 0.0
    if x >= 0 and x <= 2:
        s = 4.0 / 3 * pow(x, 1.5) - 0.4 * pow(x, 2.5) + 288.741504
    elif x > 2 and x <= 5:
        s = 0.25 * pow(x, 4) - 2.0 / 3 * pow(x, 3) - 0.5 * pow(x, 2) + 2 * x + 289.583332
    elif x > 5 and x <= 10:
        s = 72 * x - 8.0 / 15 * pow(x - 5, 1.875)
    return s
for T in range(int(input())):
    a = [int(i) for i in input().split()]
    print("%.0f" % (f(a[1]) - f(a[0])))
