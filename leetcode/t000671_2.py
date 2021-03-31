# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        self.min1 = -1
        self.min2 = -1
        self.bianli(root)
        return self.min2
    
    def bianli(self, root):
        if root != None:
            if root.val < self.min1 or self.min1 == -1:
                self.min2 = self.min1
                self.min1 = root.val
            elif self.min1 < root.val < self.min2 or (self.min2 == -1 and root.val > self.min1):
                self.min2 = root.val
            self.bianli(root.left)
            self.bianli(root.right)



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