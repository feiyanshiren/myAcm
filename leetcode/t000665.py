from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        l = len(nums)
        if l < 3:
            return True
        a = 0
        for i in range(l - 1):
            if nums[i] > nums[i + 1]:
                if i == 0:
                    nums[i] = -2147483648
                    a += 1
                else:
                    if nums[i - 1] <= nums[i + 1]:
                        nums[i] = nums[i + 1]
                        a += 1
                    else:
                        nums[i + 1] = nums[i]
                        a += 1
            if a > 1:
                return False
        return a <= 1


s = Solution()
print(s.checkPossibility([4,2,3]))
print(s.checkPossibility([4,2,1]))