import math

class Solution:
    def arrangeCoins(self, n: int) -> int:
        a = (-1 + math.sqrt(1 + 8 * n)) / 2
        return(int(a))
        
    
s = Solution()
print(s.arrangeCoins(5))
print(s.arrangeCoins(8))
print(s.arrangeCoins(0))
print(s.arrangeCoins(2147483647))
print(s.arrangeCoins(6))
print(s.arrangeCoins(2147483646))