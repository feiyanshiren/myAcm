d = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
x = d.lower()
md = {j: i + 1 for i, j in enumerate(d)}
mx = {j: -(i + 1) for i, j in enumerate(x)}
md.update(mx)
for t in range(int(input())):
    s = input().split()
    print(int(s[1]) + md[s[0]])
