from typing import List
class Solution:
    def containsDuplicate(self, nums):
        m = set()
        for i in nums:
            if i in m:
                return True
            m.add(i)
        return False
    
s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))
print(s.containsDuplicate([1, 2, 3, 4]))
print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))