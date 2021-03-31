# 解：
# 暴力法，注意严格看提议条件
#
# ```
from typing import List


class Solution:
    def numMagicSquaresInside(self, grid: List[List[int]]) -> int:
        count = 0
        l1 = len(grid)
        if l1 >= 3:
            l2 = len(grid[0])
            if l2 >= 3:
                for i in range(l1 - 2):
                    for j in range(l2 - 2):
                        if self.ifh([[grid[i][j], grid[i][j + 1], grid[i][j + 2]],
                                     [grid[i + 1][j], grid[i + 1][j + 1], grid[i + 1][j + 2]],
                                     [grid[i + 2][j], grid[i + 2][j + 1], grid[i + 2][j + 2]]]):
                            count += 1
        return count

    def ifh(self, grid):
        a = []
        for i in range(3):
            for j in range(3):
                if grid[i][j] <= 0:
                    return False
                if grid[i][j] > 9:
                    return False
                if grid[i][j] in a:
                    return False
                a.append(grid[i][j])
        m1 = grid[0][0] + grid[0][1] + grid[0][2]
        m2 = grid[1][0] + grid[1][1] + grid[1][2]
        m3 = grid[2][0] + grid[2][1] + grid[2][2]
        m4 = grid[0][0] + grid[1][0] + grid[2][0]
        m5 = grid[0][1] + grid[1][1] + grid[2][1]
        m6 = grid[0][2] + grid[1][2] + grid[2][2]
        m7 = grid[0][0] + grid[1][1] + grid[2][2]
        m8 = grid[0][2] + grid[1][1] + grid[2][0]
        if m1 == m2 and m1 == m3 and m1 == m4 and m1 == m5 and m1 == m6 \
                and m1 == m7 and m1 == m8:
            return True
        else:
            return False


# 840.
# 矩阵中的幻方 - -2
#
# 3
# x
# 3
# 的幻方是一个填充有从
# 1
# 到
# 9
# 的不同数字的
# 3
# x
# 3
# 矩阵，其中每行，每列以及两条对角线上的各数之和都相等。
#
# 给定一个由整数组成的
# grid，其中有多少个
# 3 × 3
# 的 “幻方” 子矩阵？（每个子矩阵都是连续的）。
#
#
#
# 示例：
#
# 输入: [[4, 3, 8, 4],
#      [9, 5, 1, 9],
#      [2, 7, 6, 2]]
# 输出: 1
# 解释:
# 下面的子矩阵是一个
# 3
# x
# 3
# 的幻方：
# 438
# 951
# 276
#
# 而这一个不是：
# 384
# 519
# 762
#
# 总的来说，在本示例所给定的矩阵中只有一个
# 3
# x
# 3
# 的幻方子矩阵。
#
# 提示:
#
# 1 <= grid.length <= 10
# 1 <= grid[0].length <= 10
# 0 <= grid[i][j] <= 15

# 解：
# 打表发，其实中心是5，才可能是幻
#
# ```


class Solution(object):
    def numMagicSquaresInside(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        l = [[8, 1, 6, 3, 5, 7, 4, 9, 2], [6, 1, 8, 7, 5, 3, 2, 9, 4], [4, 9, 2, 3, 5, 7, 8, 1, 6],
             [2, 9, 4, 7, 5, 3, 6, 1, 8], [6, 7, 2, 1, 5, 9, 8, 3, 4], [8, 3, 4, 1, 5, 9, 6, 7, 2],
             [2, 7, 6, 9, 5, 1, 4, 3, 8], [4, 3, 8, 9, 5, 1, 2, 7, 6]]
        count = 0
        for i in range(len(grid) - 2):
            for j in range(len(grid[0]) - 2):
                temp = grid[i][j:j + 3] + grid[i + 1][j:j + 3] + grid[i + 2][j:j + 3]
                if temp in l:
                    count += 1
        return count
