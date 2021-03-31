# 解：
# 模拟实现，效率低 ，要注意头尾都是0的情况
from typing import List


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res = 0
        ll = len(seats)
        for i in range(ll):
            cz = 0
            cy = 0
            if seats[i] == 0:
                b = 0
                for j in range(i - 1, -1, -1):
                    cz += 1
                    if seats[j] == 1:
                        b = 1
                        break
                if b == 0:
                    cz = 20000
                b = 0
                for j in range(i + 1, ll):
                    cy += 1
                    if seats[j] == 1:
                        b = 1
                        break
                if b == 0:
                    cy = 20000
                mm = min(cz, cy)
                res = max(res, mm)
        return res


# 解：
# 转字符串分组法


class Solution(object):
    def maxDistToClosest(self, seats):
        str_seats = ''.join(str(x) for x in seats)  # list->str
        empty = str_seats.split('1')  # str用1分隔
        max_empty = max(len(x) for x in empty)
        return max((max_empty + 1) // 2, len(empty[0]), len(empty[-1]))  # 考虑最左和最右


# 849. 到最近的人的最大距离    --3
#
# 在一排座位（ seats）中，1 代表有人坐在座位上，0 代表座位上是空的。
#
# 至少有一个空座位，且至少有一人坐在座位上。
#
# 亚历克斯希望坐在一个能够使他与离他最近的人之间的距离达到最大化的座位上。
#
# 返回他到离他最近的人的最大距离。
#
# 示例 1：
#
# 输入：[1,0,0,0,1,0,1]
# 输出：2
# 解释：
# 如果亚历克斯坐在第二个空位（seats[2]）上，他到离他最近的人的距离为 2 。
# 如果亚历克斯坐在其它任何一个空位上，他到离他最近的人的距离为 1 。
# 因此，他到离他最近的人的最大距离是 2 。
#
# 示例 2：
#
# 输入：[1,0,0,0]
# 输出：3
# 解释：
# 如果亚历克斯坐在最后一个座位上，他离最近的人有 3 个座位远。
# 这是可能的最大距离，所以答案是 3 。
#
# 提示：
#
#     1 <= seats.length <= 20000
#     seats 中只含有 0 和 1，至少有一个 0，且至少有一个 1。
#
# 解：
# 快慢双指针法


class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        res = 0
        p1 = None
        for p2 in range(len(seats)):
            if seats[p2] == 1:
                if p1 is None:  # 考虑起始为0情况
                    res = max(res, p2)
                else:
                    res = max(res, int((p2 - p1) / 2))
                p1 = p2
        if seats[p2] == 0:  # 考虑末尾为0情况
            res = max(res, p2 - p1)
        return res
