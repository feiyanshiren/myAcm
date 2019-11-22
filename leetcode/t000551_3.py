import re

class Solution:
    def checkRecord(self, s: str) -> bool:
        if re.match(".*A.*A|.*LLL.*", s):
            return False
        return True

s = Solution()
print(s.checkRecord("PPALLP"))
print(s.checkRecord("PPALLL"))
print(s.checkRecord("PPALLLLP"))
print(s.checkRecord("PPALLPA"))