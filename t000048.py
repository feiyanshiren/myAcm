m = int(input())
s = list({int(i): 0 for i in input().split()}.keys())
s.sort()
p = ""
for i in s:
    p = p + str(i) + " "
print(len(s))
print(p.strip())
