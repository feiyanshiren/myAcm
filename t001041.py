def dis(s1, ss2, d):
    s11 = [int(i) for i in s1.split()]
    for sss in ss2:
        s22 = [int(i) for i in sss.split()]
        sp = abs(s22[0] - s11[0])
        cz = abs(s22[1] - s11[1])
        if sp <= d and cz <= d:
            return True
    return False


t = int(input())
for i in range(t):
    n = [int(k) for k in input().split()]
    s = []
    for d in range(n[3]):
        s.append(input())
    if len(s) == 0:
        break
    pp = s.pop()
    q = {pp: [pp]}
    while len(s) != 0:
        sd = []
        for ss in s:
            for k in q:
                if dis(ss, q[k], n[2]):
                    q[k].append(ss)
                    sd.append(ss)
        if len(sd) != 0:
            for i in sd:
                s.remove(i)
        else:
            ppp = s.pop()
            q[ppp] = [ppp]
    d = len(q.keys())
    if d % n[1] == 0:
        b = int(d / n[1])
    else:
        b = int(d / n[1]) + 1
    print(b)
