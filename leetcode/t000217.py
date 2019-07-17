class Solution:
    def containsDuplicate(self, nums):
        m = {}
        for i in nums:
            f = m.get(i, 0) + 1
            if f > 1:
                return True
            m[i] = f
        return False
   
s = Solution()
print(s.containsDuplicate([1, 2, 3, 1]))
print(s.containsDuplicate([1, 2, 3, 4]))
print(s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2]))