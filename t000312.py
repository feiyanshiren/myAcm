import datetime


def ifr(i):
    if i % 4 == 0 and i % 100 != 0 or i % 400 == 0:
        return True
    else:
        return False


for t in range(int(input())):
    s = [int(i) for i in input().split("-")]
    if s[1] == 2 and s[2] == 29:
        if not ifr(s[0] + 20):
            print(-1)
            break
    d = datetime.datetime(s[0], s[1], s[2])
    d2 = datetime.datetime(s[0] + 20, s[1], s[2])
    print((d2 - d).days)
