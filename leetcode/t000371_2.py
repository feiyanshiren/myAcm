class Solution:
    def getSum(self, a: int, b: int) -> int:
        s1 = str(a)
        s2 = str(b)
        s = "+".join([s1, s2])
        return eval(s)
    
s = Solution()
print(s.getSum(1, 2))
print(s.getSum(-2, 3))