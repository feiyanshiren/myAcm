import re
for i in range(int(input())):
    s = input()
    if len(s) == 5: print(3)
    else:
        k = re.match(r"(.ne)|(o.e)|(on.)", s)
        if k is None: print(2)
        else: print(1)