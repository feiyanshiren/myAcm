d = [1, 4, 10, 22, 46, 94, 190, 382, 766, 1534, 3070, 6142, 12286, 24574,
     49150, 98302, 196606, 393214, 786430, 1572862, 3145726, 6291454, 12582910,
     25165822, 50331646, 100663294, 201326590, 402653182, 805306366]
n = int(input())
f = []
for i in range(n):
    m = int(input())
    f.append(d[m])
for i in f:
    print(i)
