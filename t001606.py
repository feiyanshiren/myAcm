import math
try:
    while 1:
        s = 0
        for i in range(1, int(input()) + 1):
            s += math.factorial(i)
        print(s)
except:
    pass