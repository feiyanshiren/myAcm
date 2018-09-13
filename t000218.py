import re
try:
    while 1:
        s = re.findall(r"bowl|knife|fork|chopsticks", input())
        d = {i: 0 for i in s}
        for i in d.keys():
            print(i, end=" ")
        print()
except Exception:
    pass
