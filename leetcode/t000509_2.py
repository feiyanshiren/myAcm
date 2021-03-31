from functools import lru_cache

class Solution:
    @lru_cache(maxsize=30)
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)
    
s = Solution()

import time
t = time.time()
for i in range(100):
    print(s.fib(30))
print(time.time() - t)