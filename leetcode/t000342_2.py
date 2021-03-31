class Solution:
    def __init__(self):
        self.a = set()
        i = 1
        while i <= 1162261467:
            self.a.add(i)
            i *= 4
            
    def isPowerOfFour(self, n: int) -> bool:
        if n in self.a:
            return True
        else:
            return False
    

s = Solution()
print(s.isPowerOfFour(16))
print(s.isPowerOfFour(1))
print(s.isPowerOfFour(0))
print(s.isPowerOfFour(5))