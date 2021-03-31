class Solution:
    def fib(self, N: int) -> int:
        if N < 2:
            return N
        p = 0
        c = 1
        for i in range(N - 1):
            s = p + c
            p = c
            c = s
        return c
                
s = Solution()

import time
t = time.time()
for i in range(100):
    print(s.fib(30))
print(time.time() - t)