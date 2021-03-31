# 836. 矩形重叠
#
# 矩形以列表 [x1, y1, x2, y2] 的形式表示，其中 (x1, y1) 为左下角的坐标，(x2, y2) 是右上角的坐标。
#
# 如果相交的面积为正，则称两矩形重叠。需要明确的是，只在角或边接触的两个矩形不构成重叠。
#
# 给出两个矩形，判断它们是否重叠并返回结果。
#
# 示例 1：
#
# 输入：rec1 = [0,0,2,2], rec2 = [1,1,3,3]
# 输出：true
#
# 示例 2：
#
# 输入：rec1 = [0,0,1,1], rec2 = [1,0,2,1]
# 输出：false
#
# 说明：
#
#     两个矩形 rec1 和 rec2 都以含有四个整数的列表的形式给出。
#     矩形中的所有坐标都处于 -10^9 和 10^9 之间。
#
#
# 解：
# 如果两个矩形相交，那么矩形A B的中心点和矩形的边长是有一定关系的。
#
# Case 2345中，两个中心点间的距离肯定小于AB边长和的一半。
#
# Case 1中就像等了。
#
# 设A[x01,y01,x02,y02]  B[x11,y11,x12,y12].
#
# 矩形A和矩形B物理中心点X方向的距离为Lx：abs( (x01+x02)/2 – (x11+x12) /2)
#
# 矩形A和矩形B物理中心点Y方向的距离为Ly：abs( (y01+y02)/2 – (y11+y12) /2)
#
# 矩形A和矩形B X方向的边长为 Sax：abs(x01-x02)  Sbx: abs(x11-x12)
#
# 矩形A和矩形B Y方向的边长为 Say：abs(y01-y02)  Sby: abs(y11-y12)
#
# 如果AB相交，则满足下列关系：
#
# Lx <= (Sax + Sbx)/2 && Ly <=(Say+ Sby)/2
# ```
from typing import List


class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        zx = abs(rec1[0] + rec1[2] - rec2[0] - rec2[2])
        x = abs(rec1[0] - rec1[2]) + abs(rec2[0] - rec2[2])
        zy = abs(rec1[1] + rec1[3] - rec2[1] - rec2[3])
        y = abs(rec1[1] - rec1[3]) + abs(rec2[1] - rec2[3])
        if zx < x and zy < y:
            return True
        else:
            return False