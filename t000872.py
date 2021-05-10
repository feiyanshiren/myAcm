import math
try:
    while 1:
        t = ""
        n = [int(i) for i in input().split()]
        m = [int(i) for i in input().split()]
        for i in range(n[1]):
            j = math.factorial(n[0]) /\
             (math.factorial(m[i]) * math.factorial(n[0] - m[i]))
            t = t + str(int(j)) + " "
            n[0] = n[0] - m[i]
        print(t.strip())
except Exception:
    pass
