def cc(x, k, t):
    x = ord(x) - ord("A")
    for i in range(26):
        if (k * i + t) % 26 == x: return chr(i + ord("A"))
def ss(x, k, t):
    x = list(x)
    for i in range(len(x)): x[i] = cc(x[i], k, t)
    print("".join(x))
try:
    while 1:
        s = input().split()
        ss(s[0], int(s[1]), int(s[2]))
except: pass