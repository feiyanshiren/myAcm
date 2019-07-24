class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in m:
                return [m[a], i]
            m[nums[i]] = i

s = Solution()
print(s.twoSum([3, 3], 6))