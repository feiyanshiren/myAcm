from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        l1 = len(g)
        l2 = len(s)
        g.sort()
        s.sort()
        a = 0
        i = 0
        j = 0
        while i < l1 and j < l2:
            if g[i] <= s[j]:
                a += 1
                i += 1
                j += 1
            else:
                j += 1
        return a
    
s = Solution()
print(s.findContentChildren([1, 2, 3], [1, 1]))
print(s.findContentChildren([1, 2,], [1, 2, 3]))