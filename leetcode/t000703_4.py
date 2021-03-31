from typing import List
import bisect

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        self.nums = nums[-self.k:]
        

    def add(self, val: int) -> int:
        bisect.insort(self.nums, val)
        self.nums = self.nums[-self.k:]
        return self.nums[0]
        


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)

k = 3
arr = [4,5,8,2]
kthLargest1 = KthLargest(3, arr)
print(kthLargest1.add(3))   # returns 4
print(kthLargest1.add(5))   # returns 5
print(kthLargest1.add(10))   # returns 5
print(kthLargest1.add(9))    # returns 8
print(kthLargest1.add(4))    # returns 8



