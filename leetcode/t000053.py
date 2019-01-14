class Solution:
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        h = nums[0]
        s = 0
        for i in nums:
            s += i
            if s > h:
                h = s
            if s < 0:
                s = 0
        return h

        