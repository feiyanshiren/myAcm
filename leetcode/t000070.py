import functools
import time
# import sys
# sys.setrecursionlimit(1000000)
class Solution:
    @functools.lru_cache()
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 2
        else:
            return self.climbStairs(n - 1) + self.climbStairs(n - 2)

s = Solution()
t = time.time()
print(s.climbStairs(0))
print(s.climbStairs(1))
print(s.climbStairs(2))
print(s.climbStairs(3))
print(s.climbStairs(4))
print(s.climbStairs(5))
print(s.climbStairs(6))
print(s.climbStairs(7))
print(s.climbStairs(8))
print(s.climbStairs(9))
print(s.climbStairs(10))
print(s.climbStairs(100))
print(time.time() - t)
