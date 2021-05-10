from operator import mul
from functools import reduce
try:
    while 1:
        print(reduce(mul, range(1, int(input()) + 1)))
except:
    pass