# a = input()
# b = a.split()
c = [int(i) for i in input().split()]
# c = [int(b[0]), int(b[1]), int(b[2])]
c.sort()
print("%d %d %d" % (c[0], c[1], c[2]))