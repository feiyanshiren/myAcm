# 836. 矩形重叠    --3
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
# 检查区域
#
# 想法
#
# 如果两个长方形重合，那么就一个区域。这个区域一定是一个长方形，并且所有坐标都是正数，因为交点的边界都是坐标定义的。
#
# 因此，我们将问题看作一个一维问题，两条线段是否重合。
#
# 算法
#
# 假设交点区域是 width * height，其中 width 是交点区域在 x 轴上的投影，height 是在 y 轴上的投影。我们希望这两个量都是正数。
#
# width 是正数当 min(rec1[2], rec2[2]) > max(rec1[0], rec2[0])，也就是大 x 坐标的较小值大于小 x 坐标的较大值。height 也同理。
#
#
# ```
class Solution(object):
    def isRectangleOverlap(self, rec1, rec2):
        def intersect(p_left, p_right, q_left, q_right):
            return min(p_right, q_right) > max(p_left, q_left)
        return (intersect(rec1[0], rec1[2], rec2[0], rec2[2]) and # width > 0
                intersect(rec1[1], rec1[3], rec2[1], rec2[3]))    # height > 0