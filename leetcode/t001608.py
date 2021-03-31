from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        max_num = max(nums)
        for i in range(max_num + 1):
            count = 0
            for j in nums:
                if j >= i:
                    count += 1
            if count == i:
                return i
        return -1

s = Solution()
print(s.specialArray([3, 5]))
print(s.specialArray([0,0]))
print(s.specialArray([0,4,3,0,4]))
print(s.specialArray([3,6,7,7,0]))