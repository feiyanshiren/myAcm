for i in range(int(input())):
    f = {
        "Monday": 0, "Tuesday": 0, "Wednesday": 0,
        "Thursday": 0, "Friday": 0, "Saturday": 0,
        "Sunday": 0
    }
    s = [int(d) for d in input().split()]
    s.sort()
    kk = list(f.keys())
    ll = len(s)
    for k in range(ll):
        f[kk[k]] = s[k]
    print(f[input().strip()])
