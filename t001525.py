from datetime import datetime
for T in range(int(input())):
    s = [datetime.strptime(i, '%Y-%m-%d') for i in input().split()]
    if s[1] < s[2]:
        if s[0] >= s[1] and s[0] <= s[2]:
            print("YES")
            continue
    print("NO")
