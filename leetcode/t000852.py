#
# 解：其实就是找最大值嘛
#
# ```
from typing import List


class Solution:

    def peakIndexInMountainArray(self, A: List[int]) -> int:
        return A.index(max(A))


#
# 解：顺序查大于后一个值的
#
# ```


class Solution:

    def peakIndexInMountainArray(self, A: List[int]) -> int:
        for i in range(len(A) - 1):
            if A[i] > A[i + 1]:
                return i


# 852.
# 山脉数组的峰顶索引 - -3
#
# 我们把符合下列属性的数组
# A
# 称作山脉：
#
# A.length >= 3
# 存在
# 0 < i < A.length - 1
# 使得A[0] < A[1] < ...
# A[i - 1] < A[i] > A[i + 1] > ... > A[A.length - 1]
#
# 给定一个确定为山脉的数组，返回任何满足
# A[0] < A[1] < ...
# A[i - 1] < A[i] > A[i + 1] > ... > A[A.length - 1]
# 的
# i
# 的值。
#
#
#
# 示例
# 1：
#
# 输入：[0, 1, 0]
# 输出：1
#
# 示例
# 2：
#
# 输入：[0, 2, 1, 0]
# 输出：1
#
# 提示：
#
# 3 <= A.length <= 10000
# 0 <= A[i] <= 10 ^ 6
# A
# 是如上定义的山脉
#
# 解：二分法
#
# ```


class Solution:

    def peakIndexInMountainArray(self, A: List[int]) -> int:
        l = 0
        r = len(A) - 1
        while l <= r:
            mid = (l + r) // 2
            if A[mid - 1] < A[mid] < A[mid + 1]:
                l = mid + 1
            elif A[mid - 1] > A[mid] > A[mid + 1]:
                r = mid - 1
            else:
                return mid
