m = [0]
k = 0
for i in range(1, 1000001):
    if "0" in str(i): k += 1
    m.append(i - k)
try:
    while 1:
        s = input()
        if "0" in s: print("Unlucky")
        else: print(m[int(s)])
except: pass