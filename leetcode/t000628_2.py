from typing import List

class Solution:
    def maximumProduct(self, nums: List[int]) -> int:
        if len(nums) == 3:
            return nums[0] * nums[1] * nums[2]
        mi1 = 2147483647
        mi2 = 2147483647
        ma1 = -2147483648
        ma2 = -2147483648
        ma3 = -2147483648
        for i in nums:
            if i <= mi1:
                mi2 = mi1
                mi1 = i
            elif i <= mi2:
                mi2 = i
            if i >= ma1:
                ma3 = ma2
                ma2 = ma1
                ma1 = i
            elif i >= ma2:
                ma3 = ma2
                ma2 = i
            elif i >= ma3:
                ma3 = i
        return max(mi1 * mi2 * ma1, ma1 * ma2 * ma3)
        


s = Solution()
print(s.maximumProduct([1,2,3]))
print(s.maximumProduct([1,2,3,4]))
