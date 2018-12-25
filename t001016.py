class Node:
    def __init__(self):
        self.x = 0
        self.y = 0
        
class St:
    def __init__(self):
        self.a = Node()
        self.b = Node()
        
st = [St(), St()]

def ju():
    if min(st[0].a.x, st[0].b.x) > max(st[1].a.x, st[1].b.x):
        return False
    if min(st[1].a.x, st[1].b.x) > max(st[0].a.x, st[0].b.x):
        return False
    if min(st[0].a.y, st[0].b.y) > max(st[1].a.y, st[1].b.y):
        return False
    if min(st[1].a.y, st[1].b.y) > max(st[0].a.y, st[0].b.y):
        return False
    k = float((st[0].a.x-st[1].a.x)*(st[1].b.y-st[1].a.y)-(st[0].a.y-st[1].a.y)*(st[1].b.x-st[1].a.x))
    l = float((st[0].b.x-st[1].a.x)*(st[1].b.y-st[1].a.y)-(st[0].b.y-st[1].a.y)*(st[1].b.x-st[1].a.x))
    m = float((st[1].a.x-st[0].a.x)*(st[0].b.y-st[0].a.y)-(st[1].a.y-st[0].a.y)*(st[0].b.x-st[0].a.x))
    n = float((st[1].b.x-st[0].a.x)*(st[0].b.y-st[0].a.y)-(st[1].b.y-st[0].a.y)*(st[0].b.x-st[0].a.x))
    if k * l <= 0 and m * n <= 0:
        return True
    else:
        return False

for T in range(int(input())):
    s = [float(i) for i in input().split()]
    st[0].a.x = s[0]
    st[0].a.y = s[1]
    st[0].b.x = s[2]
    st[0].b.y = s[3]
    st[1].a.x = s[4]
    st[1].a.y = s[5]
    st[1].b.x = s[6]
    st[1].b.y = s[7]
    if ju():
        print("Interseetion")
    else:
        print("Not Interseetion")
    