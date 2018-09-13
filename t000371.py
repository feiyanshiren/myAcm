class rbt:
    def __init__(self, s):
        self.xy = [0, 0]
        self.f = [0, 1]
        self.mp = {"[0, 1]": "N", "[-1, 0]": "W", "[0, -1]": "S", "[1, 0]": "E"}
        self.mp1 = {"L": self.tl, "R": self.tr, "M": self.mv}
        self.ls = [[0, 1], [-1, 0], [0, -1], [1, 0]]
        for i in s: self.mp1[i]()
    def tr(self):
        self.f = self.ls[self.ls.index(self.f) - 1]
    def tl(self):
        a = self.ls.index(self.f) + 1
        a = 0 if a >= 4 else a
        self.f = self.ls[a]
    def mv(self):
        self.xy[0] += self.f[0]
        self.xy[1] += self.f[1]
for T in range(int(input())):
    c = rbt(input())
    print("%d %d %s" % (c.xy[0], c.xy[1], c.mp[str(c.f)]))
