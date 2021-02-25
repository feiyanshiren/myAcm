

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:

        res1 = []
        res2 = []

        def s(node, res):
            if not node:
                return
            else:
                if not node.left and not node.right:
                    res.append(node.val)
                else:
                    s(node.left, res)
                    s(node.right, res)

        s(root1, res1)
        s(root2, res2)
        return res1 == res2


# ```
# ---
#
# 872.
# 叶子相似的树 - -2
#
# 请考虑一颗二叉树上所有的叶子，这些叶子的值按从左到右的顺序排列形成一个
# 叶值序列 。
#
# 举个例子，如上图所示，给定一颗叶值序列为(6, 7, 4, 9, 8)
# 的树。
#
# 如果有两颗二叉树的叶值序列是相同，那么我们就认为它们是
# 叶相似
# 的。
#
# 如果给定的两个头结点分别为
# root1
# 和
# root2
# 的树是叶相似的，则返回
# true；否则返回
# false 。
#
#
#
# 提示：
#
# 给定的两颗树可能会有
# 1
# 到
# 200
# 个结点。
# 给定的两颗树上的值介于
# 0
# 到
# 200
# 之间。
#
# 解：
# 深度遍历，学习yield的使用。
#
# ```py


class Solution:
    def leafSimilar(self, root1, root2):
        def dfs(node):
            if node:
                if not node.left and not node.right:
                    yield node.val
                yield from dfs(node.left)
                yield from dfs(node.right)

        return list(dfs(root1)) == list(dfs(root2))


