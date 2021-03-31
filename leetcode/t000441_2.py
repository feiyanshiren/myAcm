import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        left = 0
        right = n
        m = 0
        su = 0
        while left < right - 1:
            m = left + (right - left) // 2
            su = m + (m * (m - 1)) // 2
            if su > n:
                right = m
            elif su < n:
                left = m
            else:
                return m
        if su > n:
            return m - 1
        return m
        
    
s = Solution()
print(s.arrangeCoins(5))
print(s.arrangeCoins(8))
print(s.arrangeCoins(0))
print(s.arrangeCoins(2147483647))
print(s.arrangeCoins(6))
print(s.arrangeCoins(2147483646))