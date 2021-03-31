# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def trimBST(self, root, L, R):
        def trim(node):
            if not node:
                return None
            elif node.val > R:
                return trim(node.left)
            elif node.val < L:
                return trim(node.right)
            else:
                node.left = trim(node.left)
                node.right = trim(node.right)
                return node

        return trim(root)


"""
令 trim(node) 作为该节点上的子树的理想答案。我们可以递归地构建该答案。

算法

当 node.val > R\text{node.val > R}node.val > R，那么修剪后的二叉树必定出现在节点的左边。

类似地，当 node.val < L\text{node.val < L}node.val < L，那么修剪后的二叉树出现在节点的右边。否则，我们将会修剪树的两边。

"""


s = Solution()

t1 = TreeNode(1)
t2 = TreeNode(0)
t3 = TreeNode(2)

t4 = TreeNode(3)
t5 = TreeNode(0)
t6 = TreeNode(4)
t7 = TreeNode(2)
t8 = TreeNode(1)

t1.left = t2
t1.right = t3

t4.left = t5
t4.right = t6

t5.right = t7
t7.left = t8

print(s.trimBST(t1, 1, 2))
print(s.trimBST(t4, 1, 3))

