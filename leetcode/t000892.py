from typing import List


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        l = len(grid)
        m = 0
        for i in range(l):
            for j in range(l):
                y = grid[i][j]
                if y > 0:
                    m += (y << 2) + 2
                    if i > 0:
                        m -= min(y, grid[i - 1][j]) << 1
                    if j > 0:
                        m -= min(y, grid[i][j - 1]) << 1
        return m


# ```
# ---
#
# 892.
# 三维形体的表面积 - -2
#
# 在
# N * N
# 的网格上，我们放置一些
# 1 * 1 * 1
# 的立方体。
#
# 每个值
# v = grid[i][j]
# 表示
# v
# 个正方体叠放在对应单元格(i, j)
# 上。
#
# 请你返回最终形体的表面积。
#
#
#
# 示例
# 1：
#
# 输入：[[2]]
# 输出：10
#
# 示例
# 2：
#
# 输入：[[1, 2], [3, 4]]
# 输出：34
#
# 示例
# 3：
#
# 输入：[[1, 0], [0, 2]]
# 输出：16
#
# 示例
# 4：
#
# 输入：[[1, 1, 1], [1, 0, 1], [1, 1, 1]]
# 输出：32
#
# 示例
# 5：
#
# 输入：[[2, 2, 2], [2, 1, 2], [2, 2, 2]]
# 输出：46
#
# 提示：
#
# 1 <= N <= 50
# 0 <= grid[i][j] <= 50
#
# 解：
# 做法：
#
# 首先，一个柱体一个柱体的看，每个柱体是由：2
# 个底面（上表面 / 下表面）+ 所有的正方体都贡献了4个侧表面积。
#
# 然后，把柱体贴合在一起之后，我们需要把贴合的表面积给减掉，两个柱体贴合的表面积就是
# 两个柱体高的最小值 * 2。
#
#
# ```py


class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        l = len(grid)
        l2 = len(grid[0])
        m = 0
        for i in range(l):
            for j in range(l2):
                if grid[i][j] != 0:
                    m += grid[i][j] * 4 + 2
                if i > 0:
                    m -= min(grid[i][j], grid[i - 1][j]) * 2
                if j > 0:
                    m -= min(grid[i][j], grid[i][j - 1]) * 2
        return m

