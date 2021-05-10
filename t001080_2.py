import sys
n = int(input())
a = [0 for i in range(151)]
for i in range(n):
    k = sys.stdin.read(2)
    d = int(k.strip())
    a[d] = a[d] + 1
for i in range(151):
    for j in range(a[i]):
        sys.stdout.write("%d " % i)
sys.stdout.write("\n")
