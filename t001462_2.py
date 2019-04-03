import math

for T in range(int(input())):
    n = [int(i) for i in input().split()]
    a = math.floor(math.sqrt(n[0]))
    b = math.floor(math.sqrt(n[1]))
    print(a * b)
