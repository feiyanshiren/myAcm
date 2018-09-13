# 输出格式有错误
def qukuohc(ss):
    dd = ""
    kk = ""
    k = 0
    for sss in ss:
        if k == 0:
            if sss == "(":
                k = 1
                continue
            else:
                dd = dd + sss
        else:
            if sss == ")":
                k = 0
                continue
            else:
                kk = kk + sss
    if dd != "" and kk == "":
        return [dd]
    else:
        return [dd, kk]


n = int(input())
f = []
count = 0
ti = []
titi = []
tr = []
for i in range(n * 3):
    tt2 = []
    k = input()
    if count == 0:
        count = count + 1
    elif count == 1:
        ti.append(k)
        count = count + 1
    else:
        if k == "True":
            t_ti = ti[len(ti) - 1].split("|")
            for t_ti_in in t_ti:
                tt2.append(qukuohc(t_ti_in))
        else:
            tttt = ti[len(ti) - 1].split("|")
            tttt2 = []
            for tttt_in in tttt:
                tttt2.extend(qukuohc(tttt_in))
            for i in range(len(tttt)):
                tt2.append(tttt2)
        tr.append(k)
        titi.append(tt2)
        count = 0


m = int(input())
# da = []
count = 0
tim = []
for i in range(n * m):
    k = input().split("|")
    tim.append(k)
    if count < n - 1:
        count = count + 1
    else:
        # da.append(tim)
        k = tim

        da22 = []
        for i in range(len(k)):
            da_in = k[i]
            if tr[i] == "True":
                da22.append(da_in)
            else:
                d3 = []
                for da_in_in in da_in:
                    if da_in_in in d3:
                        d3.append("")
                    else:
                        d3.append(da_in_in)
                da22.append(d3)

        dac = []

        da_in = da22
        count = 0
        for i in range(len(da_in)):
            da_in_in = da_in[i]
            for k in range(len(titi[i])):
                da_in_in_in = da_in_in[k]
                titi_in = titi[i][k]
                if da_in_in_in in titi_in:
                    count = count + 1
                    if tr[i] == "False":
                        for e in range(len(da_in_in)):
                            ddd = da_in_in[e]
                            if ddd == da_in_in_in:
                                da22[i][e] = "````"

        print(count)
        tim = []
        count = 0
