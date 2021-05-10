import math
for n in range(int(input())):
    s = [float(i) for i in input().split()]
    r = math.sqrt(s[0] ** 2 + s[1] ** 2)
    m = math.pi * r ** 2 / 2
    y = math.ceil(m / 50)
    print("Property %d: This property will begin eroding in year %d."\
          % (n + 1, y))
print("END OF OUTPUT.")
