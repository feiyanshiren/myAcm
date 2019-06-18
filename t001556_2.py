import math
for T in range(int(input())):
    a = [int(i) for i in input().split()]
    x = a[0] * a[1] // a[2]
    y = a[0] * a[2] // a[1]
    z = a[1] * a[2] // a[0]
    x = int(math.sqrt(x + 0.5))
    y = int(math.sqrt(y + 0.5))
    z = int(math.sqrt(z + 0.5))
    print(4 * (x + y + z))