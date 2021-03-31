class Solution:
    def fib(self, N: int) -> int:
        if N == 0:
            return 0
        elif N == 1:
            return 1
        else:
            return self.fib(N - 1) + self.fib(N - 2)
    
s = Solution()
print(s.fib(2))
print(s.fib(3))
print(s.fib(4))
print(s.fib(0))
import time
t = time.time()
for i in range(100):
    print(s.fib(30))
print(time.time() - t)