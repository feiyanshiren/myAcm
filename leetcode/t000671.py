# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        a = [root]
        b = set()
        while len(a) != 0:
            c = a.pop()
            if c:
                b.add(c.val)
            if c.left:
                a.append(c.left)
            if c.right:
                a.append(c.right)
        if len(b) < 2:
            return -1
        else:
            d = list(b)
            d.sort()
            return d[1]


s = Solution()


t1 = TreeNode(2)
t2 = TreeNode(2)
t3 = TreeNode(5)
t4 = TreeNode(5)
t5 = TreeNode(6)

t6 = TreeNode(2)
t7 = TreeNode(2)
t8 = TreeNode(2)

t1.left = t2
t1.right = t3

t3.left = t4
t3.right = t5

t6.left = t7
t6.right = t8


print(s.findSecondMinimumValue(t1))
print(s.findSecondMinimumValue(t6))
