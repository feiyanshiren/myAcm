import math
for t in range(int(input())):
    n = int(input())
    s = [int(i) for i in input().split()]
    s.sort()
    print(s[math.floor(n / 2)])
