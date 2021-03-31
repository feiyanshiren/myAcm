# 812. 最大三角形面积
#
# 给定包含多个点的集合，从其中取三个点组成三角形，返回能组成的最大三角形的面积。
#
# 示例:
# 输入: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
# 输出: 2
# 解释:
# 这五个点如下图所示。组成的橙色三角形是最大的，面积为2。
#
# 注意:
#
#     3 <= points.length <= 50.
#     不存在重复的点。
#      -50 <= points[i][j] <= 50.
#     结果误差值在 10^-6 以内都认为是正确答案。
#
# 解:
# 使用面积行列式公式,循环暴力
#
# ```
from typing import List


class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        ll = len(points)
        m = 0
        for i in range(ll):
            for j in range(i + 1, ll):
                for k in range(j + 1, ll):
                    m = max(m, self.ara(points[i], points[j], points[k]))
        return m

    def ara(self, a, b, c):
        return abs(a[0] * b[1] + a[1] * c[0] + b[0] * c[1] - b[1] * c[0] - a[1] * b[0] - a[0] * c[1]) / 2