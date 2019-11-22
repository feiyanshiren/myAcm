class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") > 1 or s.find("LLL") != -1:
            return False
        return True

s = Solution()
print(s.checkRecord("PPALLP"))
print(s.checkRecord("PPALLL"))
print(s.checkRecord("PPALLLLP"))
print(s.checkRecord("PPALLPA"))