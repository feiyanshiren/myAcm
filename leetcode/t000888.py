from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sa = sum(A)
        sb = sum(B)
        for i in range(len(A)):
            for j in range(len(B)):
                if sa - A[i] + B[j] == sb - B[j] + A[i]:
                    return [A[i], B[j]]
        return []


# 使用set也超时
class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sa = sum(A)
        sb = sum(B)
        aa = set(A)
        bb = set(B)
        for i in aa:
            for j in bb:
                if sa - i + j == sb - j + i:
                    return [i, j]
        return []


# ```
# ---
#
# 888.
# 公平的糖果交换 - -2
#
# 爱丽丝和鲍勃有不同大小的糖果棒：A[i]
# 是爱丽丝拥有的第
# i
# 块糖的大小，B[j]
# 是鲍勃拥有的第
# j
# 块糖的大小。
#
# 因为他们是朋友，所以他们想交换一个糖果棒，这样交换后，他们都有相同的糖果总量。（一个人拥有的糖果总量是他们拥有的糖果棒大小的总和。）
#
# 返回一个整数数组
# ans，其中
# ans[0]
# 是爱丽丝必须交换的糖果棒的大小，ans[1]
# 是
# Bob
# 必须交换的糖果棒的大小。
#
# 如果有多个答案，你可以返回其中任何一个。保证答案存在。
#
#
#
# 示例
# 1：
#
# 输入：A = [1, 1], B = [2, 2]
# 输出：[1, 2]
#
# 示例
# 2：
#
# 输入：A = [1, 2], B = [2, 3]
# 输出：[1, 2]
#
# 示例
# 3：
#
# 输入：A = [2], B = [1, 3]
# 输出：[2, 3]
#
# 示例
# 4：
#
# 输入：A = [1, 2, 5], B = [2, 4]
# 输出：[5, 4]
#
# 提示：
#
# 1 <= A.length <= 10000
# 1 <= B.length <= 10000
# 1 <= A[i] <= 100000
# 1 <= B[i] <= 100000
# 保证爱丽丝与鲍勃的糖果总量不同。
# 答案肯定存在。
#
# 解：
# 方法：方程求解
#
# 思路
#
# 如果爱丽丝交换糖果
# x，她将会期待交换具有特定量的糖果
# y
# 回来。
#
# 算法
#
# 设爱丽丝和鲍勃分别总计有
# SA, SBS_A, S_BSA​, SB​ 的糖果。
#
# 如果爱丽丝给了糖果
# xxx，并且收到了糖果
# yyy，那么鲍勃收到糖果
# xxx
# 并给出糖果
# yyy。那么，我们一定有
#
# SA−x + y = SB−y + xS_A - x + y = S_B - y + x
# SA​−x + y = SB​−y + x
#
# 对于公平的糖果交换。这意味着
#
# y = x + SB−SA2y = x + \frac
# {S_B - S_A}
# {2}
# y = x + 2
# SB​−SA​​
#
# 我们的策略很简单。对于爱丽丝拥有的每个糖果
# xxx，如果鲍勃有糖果
# y = x + SB−SA2y = x + \frac
# {S_B - S_A}
# {2}
# y = x + 2
# SB​−SA​​，我们就返回[x，y][x，y][x，y]。我们在常量时间内使用集
# Set
# 结构来检查Bob是否拥有所需的糖果
# yyy。
#
#
# ```py


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        sa = sum(A)
        sb = sum(B)
        c = (sa - sb) // 2
        aa = set(A)
        bb = set(B)
        for i in aa:
            if i - c in bb:
                return [i, i - c]
        return []


