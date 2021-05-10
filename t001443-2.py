import math
try:
    while 1:
        n = int(input())
        k = math.sqrt(n)
        s = "%.2f" % k
        if s[-1] == "0" and s[-2] == "0":
            print("YES")
        else:
            print("NO")
except:
    pass