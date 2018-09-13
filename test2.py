import time
from test4 import f
import sys

"""
def f(i):
    return i + 1
"""


"""
mm = imp.load_source("test4", "acmtest/test4.py")
f = getattr(mm, "f")
"""



t = time.time()
j = 0
for i in range(1000):
    j = sys.modules["test4"].f(j)
print(time.time() - t)
print(j)
j = sys.modules["test4"].f(j)
print(j)