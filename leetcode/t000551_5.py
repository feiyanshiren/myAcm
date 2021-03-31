class Solution:
    def checkRecord(self, s: str) -> bool:
        count_a = 0
        s_l = ""
        for i in s:
            if i == "A":
                count_a += 1
                s_l = ""
            elif i == "L":
                s_l += "L"
            else:
                s_l = ""
            if count_a > 1:
                return False
            if s_l == "LLL":
                return False
        return True
            

s = Solution()
print(s.checkRecord("PPALLP"))
print(s.checkRecord("PPALLL"))
print(s.checkRecord("PPALLLLP"))
print(s.checkRecord("PPALLPA"))