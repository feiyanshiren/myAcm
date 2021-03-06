# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:
        li = []
        self.f(root, li)
        li.sort()
        m = 9223372036854775807
        for i in range(len(li) - 1):
            a = abs(li[i] - li[i + 1])
            if a < m:
                m = a
        return m
    
    def f(self, root, li):
        if root:
            li.append(root.val)
            self.f(root.left, li)
            self.f(root.right, li)


root = TreeNode(1)
r11 = TreeNode(3)
r21 = TreeNode(2)

root.right = r11
r11.left = r21
    
s = Solution()
print(s.getMinimumDifference(root))