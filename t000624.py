f = ["West", "North", "East", "South"]
def k(c, z):
    x = f.index(c)
    if z == "0": x -= 1
    else:
        x += 1
        x %= 4
    return f[x]
try:
    while 1:
        s = input().split()
        for i in range(int(s[1])): s[0] = k(s[0], input())
        print(s[0])      
except: pass