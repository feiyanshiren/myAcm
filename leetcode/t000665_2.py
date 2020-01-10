from typing import List

class Solution:
    def checkPossibility(self, nums: List[int]) -> bool:
        length = len(nums)
        whether_have = False
        for i in range(1, length):
            if nums[i - 1] > nums[i]:
                if whether_have or ((i + 1 < length and nums[i - 1] > nums[i + 1]) and (i - 2 >= 0 and nums[i - 2] > nums[i])):
                    return False
                whether_have = True
        return True

"""
当前数字与前一个比较，如果小于前一个，考虑两种情况：

    当前位置是比较小的，凹峰，越过当前凹峰
    前一个位置是比较大的，凸峰，越过前一个凸峰

    如果当前为凹峰、前一个位置为凸峰，则无法越过，返回False
    如果出现过凹峰或者凸峰，则返回False

"""

s = Solution()
print(s.checkPossibility([4,2,3]))
print(s.checkPossibility([4,2,1]))