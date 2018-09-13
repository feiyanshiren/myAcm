def gcd(n1, n2):
    if(n1 % n2 == 0):
        return n2
    return gcd(n2, n1 % n2)


n = int(input())
for i in range(n):
    ij = [int(j) for j in input().split()]
    r1 = gcd(ij[0], ij[1])
    r2 = ij[0] * ij[1] / r1
    print("%d %d" % (r1, r2))
