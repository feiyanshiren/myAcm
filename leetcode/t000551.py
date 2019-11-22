import re

class Solution:
    def checkRecord(self, s: str) -> bool:
        if s.count("A") > 1:
            return False
        if re.match(".*LLL.*", s):
            return False
        return True

s = Solution()
print(s.checkRecord("PPALLP"))
print(s.checkRecord("PPALLL"))