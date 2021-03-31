class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            try:
               a = nums.index(target - nums[i])
               if i != a: return [i, a]
            except: continue

    
s = Solution()
print(s.twoSum([2, 7, 11, 15], 13))