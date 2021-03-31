class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        m = {j: i for i, j in enumerate(nums)}
        for i in range(len(nums)):
            a = target - nums[i]
            if a in m and m[a] != i:
                return [i, m[a]]

s = Solution()
print(s.twoSum([3, 3], 6))