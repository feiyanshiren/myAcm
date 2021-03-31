class Solution:
    def findLUSlength(self, a: str, b: str) -> int:
        if a == b:
            return -1
        else:
            l1 = len(a)
            l2 = len(b)
            if l1 > l2:
                return l1
            else:
                return l2
    

s = Solution()
print(s.findLUSlength("aba", "cdc"))