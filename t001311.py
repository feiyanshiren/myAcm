import math
for t in range(int(input())):
    s = [int(i) for i in input().split()]
    s[0] += 1
    s[1] += 1
    print(s[2] // (s[0] * s[1] // math.gcd(s[0], s[1])) * 36)
    