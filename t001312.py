import datetime
t = int(input())
for i in range(t):
    s1 = [int(i) for i in input().split("-")]
    s2 = [int(i) for i in input().split("-")]
    d1 = datetime.datetime(2016, s1[0], s1[1])
    d2 = datetime.datetime(2016, s2[0], s2[1])
    print((d2 - d1).days)
