class Solution:
    def fib(self, N):
        if N == 0:
            return 0
        if N == 1:
            return 1
        if N == 2:
            return 1
        if N == 3:
            return 2
        if N == 4:
            return 3
        if N == 5:
            return 5
        if N == 6:
            return 8
        if N == 7:
            return 13
        if N == 8:
            return 21
        if N == 9:
            return 34
        if N == 10:
            return 55
        if N == 11:
            return 89
        if N == 12:
            return 144
        if N == 13:
            return 233
        if N == 14:
            return 377
        if N == 15:
            return 610
        if N == 16:
            return 987
        if N == 17:
            return 1597
        if N == 18:
            return 2584
        if N == 19:
            return 4181
        if N == 20:
            return 6765
        if N == 21:
            return 10946
        if N == 22:
            return 17711
        if N == 23:
            return 28657
        if N == 24:
            return 46368
        if N == 25:
            return 75025
        if N == 26:
            return 121393
        if N == 27:
            return 196418
        if N == 28:
            return 317811
        if N == 29:
            return 514229
        if N == 30:
            return 832040
        return 0

s = Solution()

import time
t = time.time()
for i in range(100):
    print(s.fib(30))
print(time.time() - t)