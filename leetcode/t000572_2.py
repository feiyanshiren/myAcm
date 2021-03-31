
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        ss = []
        st = []

        def pre_order(node: TreeNode, res: list):
            if node:
                res.append(',' + str(node.val))
                pre_order(node.left, res)
                pre_order(node.right, res)
            else:
                res.append(',#')

        pre_order(s, ss)
        pre_order(t, st)

        return ''.join(st) in ''.join(ss)


s1 = TreeNode(3)
t1 = TreeNode(4)

s11 = TreeNode(4)
s12 = TreeNode(5)

s21 = TreeNode(1)
s22 = TreeNode(2)

s31 = TreeNode(0)

t11 = TreeNode(1)
t12 = TreeNode(2)

s1.left = s11
s1.right = s12

s11.left = s21
s11.right = s22

s22.left = s31

t1.left = t11
t1.right = t12

s = Solution()
print(s.isSubtree(s1, t1))