class Solution:
    def addDigits(self, num: int) -> int:
        if num > 9:
            num %= 9
            return num if num else 9
        return num

s = Solution()
print(s.addDigits(99)) 