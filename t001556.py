import math
for T in range(int(input())):
    a = [int(i) for i in input().split()]
    w = int(math.sqrt(a[0] * a[1] * a[2]))
    print(4 * (w // a[0] + w // a[1] + w // a[2]))