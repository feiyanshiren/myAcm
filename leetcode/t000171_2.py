class Solution:
    def titleToNumber(self, s: str) -> int:
        n = 0
        for ch in s:
            n = n*26 + ord(ch)-64
        return n

s = Solution()
print(s.titleToNumber("A"))
print(s.titleToNumber("B"))
print(s.titleToNumber("C"))
print(s.titleToNumber("Z"))
print(s.titleToNumber("AA"))
print(s.titleToNumber("AB"))
print(s.titleToNumber("ZY"))
