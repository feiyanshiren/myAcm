# 783. 二叉搜索树结点最小距离    --2
#
# 给定一个二叉搜索树的根结点 root, 返回树中任意两节点的差的最小值。
#
# 示例：
#
# 输入: root = [4,2,6,1,3,null,null]
# 输出: 1
# 解释:
# 注意，root是树结点对象(TreeNode object)，而不是数组。
#
# 给定的树 [4,2,6,1,3,null,null] 可表示为下图:
#
#           4
#         /   \
#       2      6
#      / \
#     1   3
#
# 最小的差值是 1, 它是节点1和节点2的差值, 也是节点3和节点2的差值。
#
# 注意：
#
#     二叉树的大小范围在 2 到 100。
#     二叉树总是有效的，每个节点的值都是整数，且不重复。
#
# 解：
# 中序遍历就不需要排序了.
#
# ```
class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        a = []
        b = [root]
        while len(b) != 0:
            c = b.pop()
            if c.left:
                b.append(c.left)
            if c:
                a.append(c.val)
            if c.right:
                b.append(c.right)
        m = 4294967295
        for i in range(len(a) - 1):
            m = min(m, abs(a[i + 1] - a[i]))
        return m