a = 0
b = 0
for i in range(1, 1001):
    s = bin(i)[2:]
    d = s.count("1")
    f = s.count("0")
    if d > f:
        a += 1
    else:
        b += 1
        
print("%d %d" % (a, b))