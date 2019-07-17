# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        if not root:
            return None
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root
    

a = [TreeNode(i) for i in range(7)]
a[0].left = a[1]
a[0].right = a[2]
a[1].left = a[3]
a[1].right = a[4]
a[2].left = a[5]
a[2].right = a[6]
b = [a[0]]
while len(b):
    c = b.pop(0)
    if c.left:
        b.append(c.left)
    if c.right:
        b.append(c.right)
    print(c.val)
    
b = [a[0]]
while len(b):
    c = b.pop(0)
    if c.left:
        b.append(c.right)
    if c.right:
        b.append(c.left)
    print(c.val)
    
s = Solution()
b = [s.invertTree(a[0])]
while len(b):
    c = b.pop(0)
    if c.left:
        b.append(c.left)
    if c.right:
        b.append(c.right)
    print(c.val)