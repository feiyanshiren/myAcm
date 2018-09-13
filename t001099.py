import math


def ds(dd1, dd2):
    return math.sqrt(((dd2[1] - dd1[1]) ** 2) + ((dd2[0] - dd1[0]) ** 2))


def ek(f1, f2):
    d = abs(f1 - f2)
    if d <= 0.00000001:
        return True
    else:
        return False


def kk(dd1, dd2):
    s = dd2[1] - dd1[1]
    x = dd2[0] - dd1[0]
    if x == 0:
        return "no"
    else:
        return "%f" % (s / x)


def pk(kk1, kk2):
    if kk1 == "no":
        if kk2 == "no":
            return False
        else:
            if ek(float(kk2), 0):
                return True
            else:
                return False
    else:
        if ek(float(kk1), 0):
            if kk2 == "no":
                return True
            else:
                return False
        else:
            if ek(float(kk1) * float(kk2), -1):
                return True
            else:
                return False


t = int(input())
for i in range(t):
    d1 = input()
    d2 = input()
    d3 = input()
    d4 = input()
    dd1 = [int(k) for k in d1.split()]
    dd2 = [int(k) for k in d2.split()]
    dd3 = [int(k) for k in d3.split()]
    dd4 = [int(k) for k in d4.split()]
    d1d2 = {"point": d1 + " " + d2, "ds": ds(dd1, dd2),
            "vl1": dd1, "vl2": dd2}
    d1d3 = {"point": d1 + " " + d3, "ds": ds(dd1, dd3),
            "vl1": dd1, "vl2": dd3}
    d1d4 = {"point": d1 + " " + d4, "ds": ds(dd1, dd4),
            "vl1": dd1, "vl2": dd4}
    d2d3 = {"point": d2 + " " + d3, "ds": ds(dd2, dd3),
            "vl1": dd2, "vl2": dd3}
    d2d4 = {"point": d2 + " " + d4, "ds": ds(dd2, dd4),
            "vl1": dd2, "vl2": dd4}
    d3d4 = {"point": d3 + " " + d4, "ds": ds(dd3, dd4),
            "vl1": dd3, "vl2": dd4}
    if ek(d1d2["ds"], 0) or ek(d1d3["ds"], 0) or ek(d1d4["ds"], 0) or\
       ek(d2d3["ds"], 0) or ek(d2d4["ds"], 0) or ek(d3d4["ds"], 0):
        print("No")
    else:
        tt = [d1d2, d1d3, d1d4, d2d3, d2d4, d3d4]
        tt.sort(key=lambda x: x["ds"])
        if ek(tt[0]["ds"], tt[1]["ds"]) and ek(tt[0]["ds"], tt[2]["ds"]) and\
           ek(tt[0]["ds"], tt[3]["ds"]) and ek(tt[1]["ds"], tt[2]["ds"]) and\
           ek(tt[1]["ds"], tt[3]["ds"]) and ek(tt[2]["ds"], tt[3]["ds"]):
            kk1 = kk(tt[0]["vl1"], tt[0]["vl2"])
            kk2 = kk(tt[1]["vl1"], tt[1]["vl2"])
            kk3 = kk(tt[2]["vl1"], tt[2]["vl2"])
            kk4 = kk(tt[3]["vl1"], tt[3]["vl2"])
            pk1 = pk(kk1, kk2)
            pk2 = pk(kk1, kk3)
            pk3 = pk(kk1, kk4)
            pk4 = pk(kk2, kk3)
            pk5 = pk(kk2, kk4)
            pk6 = pk(kk3, kk4)
            cnt = 0
            if pk1:
                cnt = cnt + 1
            if pk2:
                cnt = cnt + 1
            if pk3:
                cnt = cnt + 1
            if pk4:
                cnt = cnt + 1
            if pk5:
                cnt = cnt + 1
            if pk6:
                cnt = cnt + 1
            if cnt == 4:
                print("Yes")
            else:
                print("No")
        else:
            print("No")
