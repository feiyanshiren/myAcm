from typing import List


class Solution:
    def specialArray(self, nums: List[int]) -> int:
        if nums == []:
            return 0
        n = len(nums)
        sort_nums = sorted(nums, reverse=True)
        if sort_nums[-1] >= n:
            return n

        for i in range(1, n):
            if sort_nums[i] < i <= sort_nums[i - 1]:  # 如果 nums 是特殊数组，那么其特征值 x 是 唯一的
                return i
        return -1




s = Solution()
print(s.specialArray([3, 5]))
print(s.specialArray([0,0]))
print(s.specialArray([0,4,3,0,4]))
print(s.specialArray([3,6,7,7,0]))


# 将数组逆序
# 这样 i 的意义就和 x 关联
# nums[i-1] 就是最大的 i 个数字中最小的，如果小于 i 则表示没有足够的数字大于 i
# 接下来，如果 nums[i] 小于 i ，则刚好有 i 个数字大于 i ，找到特征值

