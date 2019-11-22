class Solution:
    def checkRecord(self, s: str) -> bool:
        return s.count('A') <= 1 and 'LLL' not in s

s = Solution()
print(s.checkRecord("PPALLP"))
print(s.checkRecord("PPALLL"))
print(s.checkRecord("PPALLLLP"))
print(s.checkRecord("PPALLPA"))