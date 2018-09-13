m = int(input())
c = []
for i in range(m):
    s = input()
    n_s = ""
    for s_i in s:
        if s_i.islower():
            n_s = n_s + s_i.upper()
        elif s_i.isupper():
            n_s = n_s + s_i.lower()
    c.append(n_s)
for i in c:
    print(i)
