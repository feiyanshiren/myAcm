from typing import List


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        a = 0
        for i in g:
            for j in s:
                if i <= j:
                    s.remove(i)
                    a += 1
                    break
        return a
    
s = Solution()
print(s.findContentChildren([1, 2, 3], [1, 1]))
print(s.findContentChildren([1, 2,], [1, 2, 3]))