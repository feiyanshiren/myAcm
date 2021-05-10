T = int(input())
for i in range(T):
    s = [int(d) for d in input().split()]
    if s[0] % s[1] == 0:
        print(int(s[0] / s[1]))
    else:
        print(int(s[0] / s[1] + 1))
