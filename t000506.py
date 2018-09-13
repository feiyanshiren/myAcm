m = {}
k = 0
for i in range(1, 50001):
    if "4" not in str(i): k += 1
    m[i] = k
try:
    while 1: print(m[int(input())])
except: pass