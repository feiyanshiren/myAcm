import re
class Solution:
    def countSegments(self, s: str) -> int:
        d = s.strip()
        if d == "":
            return 0
        return len(re.split(" +", d))
    
s = Solution()
print(s.countSegments("Hello, my name is John"))
print(s.countSegments(", , , ,   a, eaefa"))
print(s.countSegments("                "))
