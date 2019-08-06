# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode):
        if root is not None:
            if root.left is None and root.right is None:
                if root.val is not None:
                    return ["%d" % root.val]
        a = self.btp(root, [])
        b = self.f(a, [])
        return b    
    
    def f(self, a, re):
        if not a:
            return []
        if len(a) == 0:
            return []
        else:
            if type(a[0]) == type(int(0)):
                b = [str(i) for i in a]
                re.append("->".join(b))
                return re
            else:
                b = []
                for i in a:
                    b.append(self.f(i, re))
                return re
        
        
    def btp(self, root: TreeNode, li):
        if not root:
            return li
        if not root.left and not root.right:
            return li
        if root.left and not root.right:
            c = [root.val, root.left.val]
            if len(li) != 0:
                c = li[::]
                c.append(root.left.val)
            a = self.btp(root.left, c)
            return a
        elif not root.left and root.right:
            c = [root.val, root.right.val]
            if len(li) != 0:
                c = li[::]
                c.append(root.right.val)
            b = self.btp(root.right, c)
            return b
        else:
            
            if len(li) != 0:
                c1 = li[::]
                c2 = li[::]
                c1.append(root.left.val)
                a = self.btp(root.left, c1)
                c2.append(root.right.val)
                b = self.btp(root.right, c2)
                return [a, b]
            else:
                c1 = [root.val, root.left.val]
                c2 = [root.val, root.right.val]
                a = self.btp(root.left, c1)
                b = self.btp(root.right, c2)
                return [a, b]
                

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
