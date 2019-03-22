import math
try:
    while 1:
        a = [float(i) for i in input().split()]
        b = math.log(math.sqrt(a[1]), a[0])
        print("%.3f" % b)    
except:
    pass