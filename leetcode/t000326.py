class Solution:
    def __init__(self):
        self.a = set()
        i = 1
        while i <= 9223372036854775807:
            self.a.add(i)
            i *= 3
            
    def isPowerOfThree(self, n: int) -> bool:
        if n in self.a:
            return True
        else:
            return False
    

s = Solution()
print(s.isPowerOfThree(27))
print(s.isPowerOfThree(0))
print(s.isPowerOfThree(9))
print(s.isPowerOfThree(45))