import random
import math
import time


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
    return [dd, kk]


def create1():
    print("1")
    print("5 2 1 10")
    for i in range(10):
        print("%d %d" % (random.randrange(1, 6), random.randrange(1, 6)))


def create2():
    print("1")
    print("1000")
    ss = ""
    for i in range(1000, 0, -1):
        ss = ss + str(i) + " "
    print(ss)
    f = open("create2", "w")
    f.write(ss)
    f.close()


def feibulaji(n):
    if n < 0:
        return 0
    elif n == 0:
        return 7
    elif n == 1:
        return 11
    else:
        return feibulaji(n - 1) + feibulaji(n - 2)


def t1102():
    for i in range(30):
        print(feibulaji(i))


def t1102_2():
    for i in range(1, 30):
        print(4 * i - 2)


def t1131(n, m):
    cnm = 1
    while m > 0:
        cnm = cnm * (n / m)
        n = n - 1
        m = m - 1
    return int(cnm)


def testDate():
    s = time.strftime("%Y-%m-%d")
    print(s)

"""
print(t1131(88888888, 2))
testDate()
# create2()
# print(qukuohc("Cc(cc)c"))
# create1()
d = "asdasdasdas"
f = d[0: len(d) - 1]
print(f)
"""

f = open("t1.txt", "+w")
s = ""
for i in range(100001):
    s =s + str(i) + " "
f.write(s)
f.close()