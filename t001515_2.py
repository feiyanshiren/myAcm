import math

pi1 = 16 * math.atan(1 / 5) - 4 * math.atan(1 / 239)
print(pi1)


def pi(acc=500):
    def red(num, ac):
        return num if ac == 0 else (num * num) / (6 + red(num + 2, ac - 1))
    return 3 + red(1, acc)

print(pi(500))

"""
import numpy as np
simpi = lambda num: len(list(filter(lambda pt: pt[0]*pt[0]+pt[1]*pt[1]<1, np.reshape(np.random.uniform(size=2*num), [num, 2]))))/float(num)*4
print(simpi(1000000))
"""

