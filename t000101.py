import math
for i in range(int(input())):
    x = [float(j) for j in input().split()]
    d = math.sqrt((x[2] - x[0]) ** 2 + (x[3] - x[1]) ** 2)
    print("%.2f" % d)
