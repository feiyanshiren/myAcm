import time
time1 = time.time()
h01 = ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9"]
h1 = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
h2 = ["11", "22", "33", "44",
      "55", "66", "77", "88", "99"]
hx3 = ["1x1", "2x2", "3x3", "4x4", "5x5",
       "6x6", "7x7", "8x8", "9x9"]
hx4 = ["1xx1", "2xx2", "3xx3", "4xx4", "5xx5",
       "6xx6", "7xx7", "8xx8", "9xx9"]
hx5 = ["1xyx1", "2xyx2", "3xyx3", "4xyx4", "5xyx5",
       "6xyx6", "7xyx7", "8xyx8", "9xyx9"]
hx6 = ["1xyyx1", "2xyyx2", "3xyyx3", "4xyyx4", "5xyyx5",
       "6xyyx6", "7xyyx7", "8xyyx8", "9xyyx9"]
h3 = []
h4 = []
h5 = []
h6 = []
hy5 = []
hy6 = []
for hx3_in in hx3:
    for h in h01:
        s = hx3_in.replace("x", h)
        h3.append(s)
for hx4_in in hx4:
    for h in h01:
        s = hx4_in.replace("x", h)
        h4.append(s)
for hx5_in in hx5:
    for h in h01:
        s = hx5_in.replace("x", h)
        hy5.append(s)
for hx6_in in hx6:
    for h in h01:
        s = hx6_in.replace("x", h)
        hy6.append(s)
for hy5_in in hy5:
    for h in h01:
        s = hy5_in.replace("y", h)
        h5.append(s)
for hy6_in in hy6:
    for h in h01:
        s = hy6_in.replace("y", h)
        h6.append(s)

h = h1 + h2 + h3 + h4 + h5 + h6
hh = []
for i in h:
    d = str(int(i) ** 2)
    k = str(int(i) ** 3)
    dd = d[::-1]
    kk = k[::-1]
    if d == dd and k == kk:
        hh.append(i)
hhh = []
ss = ""
k = 0
for h in hh:
    if k == 5:
        hhh.append(ss.strip())
        ss = h + " "
        k = 1
    else:
        ss = ss + h + " "
        k = k + 1
hhh.append(ss.strip())
for i in hhh:
    print(i)
print(time.time() - time1)
