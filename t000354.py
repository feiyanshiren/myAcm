import math
def f_a(a, b):
    return(2 * math.sqrt(a * b))
s = []
for N in range(int(input())):
    s.append(int(input()))
s.sort()
k = s.pop()
while len(s) > 0:
    k = f_a(k, s.pop())
print("%.3lf" % k)
