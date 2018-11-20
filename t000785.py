import math
while 1:
    s = [int(i) for i in input().split()]
    if s[0] == 0 and s[1] == 0: break
    print(round(math.sqrt(s[0] * s[0] + 9 * s[1] * s[1])))