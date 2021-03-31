from typing import List
import heapq

class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.k = k
        heapq.heapify(self.nums) # heapq模块实现了一个适用于Python列表的最小堆排序算法。
        while len(self.nums) > k:
            heapq.heappop(self.nums)

    def add(self, val: int) -> int:
        if len(self.nums) < self.k:
            heapq.heappush(self.nums, val) 
            # heapq.heappush(heap, item) 
            # Push the value item onto the heap, maintaining the heap invariant.
        elif val > self.nums[0]:
            heapq.heapreplace(self.nums,val)
            # heapq.heapreplace(heap, item)
            # Pop and return the smallest item from the heap, and also push the new item
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



