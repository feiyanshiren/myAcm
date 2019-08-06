class Solution:
    def canWinNim(self, n: int) -> bool:
        if n & 3:
            return True
        else:
            return False
    
s = Solution()
print(s.canWinNim(5))