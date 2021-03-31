# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        if not root:
            return []
        paths = []
        s = [(root, str(root.val))]
        while s:
            n, p = s.pop()
            if not n.left and not n.right:
                paths.append(p)
            if n.left:
                s.append((n.left, p + "->" + str(n.left.val)))
            if n.right:
                s.append((n.right, p + "->" + str(n.right.val)))
        return paths            

a = [1, 2, 3, None, 5, 6, 7, 8, 9]
# a = [1]
# a = [1, 2, 3, None, 5]

root = TreeNode(a.pop(0))

z = [root]

while len(z) != 0:
    b = z.pop(0)
    if len(a) != 0:
        c = a.pop(0)
        if c:
            b.left = TreeNode(c)
            z.append(b.left)
    if len(a) != 0:
        c = a.pop(0)
        if c:
            b.right = TreeNode(c)
            z.append(b.right)

z = [root]

while len(z) != 0:
    b = z.pop(0)
    print(b.val)
    if b.left:
        z.append(b.left)
    if b.right:
        z.append(b.right)

s = Solution()
print(s.binaryTreePaths(root))
