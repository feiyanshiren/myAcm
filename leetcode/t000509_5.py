import math

class Solution:
    def fib(self, N: int) -> int:
        return round((math.pow((1 + math.sqrt(5)) / 2, N) -  math.pow((1 - math.sqrt(5)) / 2, N)) / math.sqrt(5))
                
s = Solution()

import time
t = time.time()
for i in range(100):
    print(s.fib(30))
print(time.time() - t)