m = {}
for n in range(int(input())):
    s = input().split()
    m[s[0]] = s[2]
    m[s[1]] = s[2]
for k in range(int(input())):
    s = input().split()
    if m.get(s[0], "") != m.get(s[1], ""):
        print("Y")
    else:
        print("n")

    