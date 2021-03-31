class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        s = list(set(nums))
        s.sort()
        if len(s) > 2:
            return s[-3]
        else:
            return s[-1]
    
s = Solution()
print(s.thirdMax([3, 2, 1]))
print(s.thirdMax([1, 2]))
print(s.thirdMax([2, 2, 3, 1]))