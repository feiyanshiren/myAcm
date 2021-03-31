class NumArray:

    def __init__(self, nums):
        self.nums = [0]
        for i in nums:
            self.nums.append(self.nums[-1] + i)
        

    def sumRange(self, i: int, j: int) -> int:
        return self.nums[j + 1] - self.nums[i]
        


# Your NumArray object will be instantiated and called as such:
nums = [-2, 0, 3, -5, 2, -1]
obj = NumArray(nums)
param_1 = obj.sumRange(0, 2)
print(param_1)