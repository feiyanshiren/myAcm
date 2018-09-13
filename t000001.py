"""
a = input()
b = a.split(" ")
print(int(b[0]) + int(b[1]))
"""

print(sum([int(i) for i in input().split()]))