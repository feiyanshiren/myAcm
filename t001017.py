a = [[0, 0] for i in range(1001)]
a[1][0] = 1
a[1][1] = 8
a[2][0] = 17
a[2][1] = 73
a[3][0] = 226
a[3][1] = 674
for i in range(4, 1001):
    a[i][0] = (a[i - 1][0] * 9 + a[i - 1][1]) % 12345
    a[i][1] = (a[i - 1][0] + a[i - 1][1] * 9) % 12345
for T in range(int(input())):
    n = int(input())
    print(a[n][1])