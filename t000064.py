a = int(input())
for i in range(a):
    nm = [int(j) for j in input().split()]
    y = (nm[1] - 2 * nm[0]) / 2
    x = nm[0] - (nm[1] - 2 * nm[0]) / 2
    if x < 0 or y < 0:
        print("No answer")
        continue
    sx = str(x).split(".")
    sy = str(y).split(".")
    if int(sx[1]) != 0 or int(sy[1]) != 0:
        print("No answer")
        continue
    print("%d %d" % (x, y))
