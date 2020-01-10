# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
        if root is None:
            return None
        if root.val > R:
            return self.trimBST(root.left, L, R)
        if root.val < L:
            return self.trimBST(root.right, L, R)
        if root.val >= L and root.val <= R:
            root.left = self.trimBST(root.left, L, R)
            root.right = self.trimBST(root.right, L, R)
        return root


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

