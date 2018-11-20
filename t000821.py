n = []
for N in range(int(input())):
    n.append(int(input()))
n.sort()
j = []
o = []
for i in n:
    if i % 2 == 0: o.append(i)
    else: j.append(i)
print(abs(sum(j) - sum(o)))
    
    