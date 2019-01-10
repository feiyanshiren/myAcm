class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        i = 0
        while i < l:
            if val == nums[i]:
                del nums[i]
                l -= 1
            else:
                i += 1
        return len(nums)

s = Solution()
a =  [3,2,2,3]
v = 3
print(s.removeElement(a, v))