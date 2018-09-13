import time
import imp



t = time.time()
j = 0
for i in range(1000):
    mm = imp.load_source("test4", "acmtest/test4.py")
    f = getattr(mm, "f")
    j = f(j)
print(time.time() - t)
print(j)
