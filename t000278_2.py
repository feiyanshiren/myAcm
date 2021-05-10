#过不了，太深了。
def y(m, x):
    if m == 1: return 0
    else: return (y(m - 1, x) + x) % m


for n in range(int(input())):
    m = [int(i) for i in input().split()]
    print(y(m[0], m[1]) + 1)
