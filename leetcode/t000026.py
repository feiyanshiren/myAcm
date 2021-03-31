class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if l == 0:
            return 0
        a = nums[0]
        i = 1
        while i < l:
            if a == nums[i]:
                del nums[i]
                l -= 1
            else:
                a = nums[i]
                i += 1
        return len(nums)

s = Solution()
b = [1, 1, 2]
print(s.removeDuplicates(b))