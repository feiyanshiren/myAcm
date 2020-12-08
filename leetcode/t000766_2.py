# 解：
# 思路和算法

# 首先要想明白的是怎么判断 (r1, c1 和 (r2, c2) 这两个点属于一条对角线。通过观察可以发现，在满足 r1 - c1 == r2 - c2 的情况下，这两个点属于同一条对角线。

# 在上面的问题搞清楚的情况下，很容易就可以想到：让 groups[r-c] 存储每条对角线上遇到的第一个元素的值，如果之后遇到的任何一个值不等于之前存储的值，那么这个矩阵就不是托普利茨矩阵，否则就是。


# ```
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        groups = {}
        for r, row in enumerate(matrix):
            for c, val in enumerate(row):
                if r-c not in groups:
                    groups[r-c] = val
                elif groups[r-c] != val:
                    return False
        return True