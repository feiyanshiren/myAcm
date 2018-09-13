import time
time1 = time.time()

hh = []

for i in range(1, 1000000):
    s = str(i)
    ss = s[::-1]
    if s == ss:
        d = str(int(s) ** 2)
        k = str(int(s) ** 3)
        dd = d[::-1]
        kk = k[::-1]
        if d == dd and k == kk:
            hh.append(s)

print(time.time() - time1)
print(hh)
