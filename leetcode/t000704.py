from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = len(nums)
        left = 0
        right = l - 1
        while left <= right:
            haf = left + (right - left) // 2
            if nums[haf] == target:
                return haf
            elif target > nums[haf]:
                left = haf + 1
            else:
                right = haf - 1
        return -1

s = Solution()
import time
t = time.time()
for i in range(100000):

    print(s.search([-1,0,3,5,9,12], 9))
    print(s.search( [-1,0,3,5,9,12], 2))
print(time.time() - t)