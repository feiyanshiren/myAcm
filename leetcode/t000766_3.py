# 解：
# 检查左上邻居 【通过】

# 思路与算法那

# 对于每条对角线上的元素，按顺序有 a1,a2,a3,…,aka_1, a_2, a_3, \dots, a_ka1​,a2​,a3​,…,ak​。如果所有对角线上的元素都满足 a1=a2,a2=a3,…,ak−1=aka_1 = a_2, a_2 = a_3, \dots, a_{k-1} = a_ka1​=a2​,a2​=a3​,…,ak−1​=ak​,那么这个矩阵就是 托普利茨矩阵。

# 对于对角线上的元素来说，如果当前元素不是第一个出现的元素，那么它前面的元素一定在当前元素的左上角。可以推出，对于位于坐标 (r, c) 上的元素，只需要检查 r == 0 OR c == 0 OR matrix[r-1][c-1] == matrix[r][c] 就可以了。



# ```
class Solution(object):
    def isToeplitzMatrix(self, matrix):
        return all(r == 0 or c == 0 or matrix[r-1][c-1] == val
                   for r, row in enumerate(matrix)
                   for c, val in enumerate(row))