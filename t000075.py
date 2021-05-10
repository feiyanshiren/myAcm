import datetime
t = int(input())
for i in range(t):
    s1 = [int(i) for i in input().split()]
    d1 = datetime.datetime(s1[0], s1[1], s1[2])
    print(d1.timetuple().tm_yday)
