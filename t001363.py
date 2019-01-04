import datetime
for T in range(int(input())):
    s = input().split()
    d = datetime.datetime.strptime(s[0], "%Y%m%d")
    z = d + datetime.timedelta(days=int(s[2]))
    print("%s %d" % (z.strftime("%Y%m%d"), z.weekday() + 1))
    