m = {"+": lambda x: x + 1, "-": lambda x: x - 1}
t = int(input())
for i in range(t):
    n = int(input())
    x = 0
    for k in range(n):
        s = input()
        x = m[s[1]](x)
    print(x)
