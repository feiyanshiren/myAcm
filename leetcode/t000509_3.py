class Solution:
    def fib(self, N: int) -> int:
        d = [0, 1, 1]
        for i in range(3, N + 1):
            d.append(d[i - 1] + d[i - 2])
        return d[N]
                
s = Solution()

import time
t = time.time()
for i in range(100):
    print(s.fib(30))
print(time.time() - t)