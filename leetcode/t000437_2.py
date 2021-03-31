# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> int:
        if not root:
            return 0
        
        def f(n, s):
            l = 0
            r = 0
            t = [d + n.val for d in s] + [n.val]
            if n.left:
                l = f(n.left, t)
            if n.right:
                r = f(n.right, t)
            return t.count(sum) + l + r
        
        return f(root, [])
            
                

r0 = TreeNode(10)
r1 = TreeNode(5)
r12 = TreeNode(-3)
r2 = TreeNode(3)
r22 = TreeNode(2)
r23 = TreeNode(11)
r3 = TreeNode(3)
r32 = TreeNode(-2)
r33 = TreeNode(1)

r0.left = r1
r0.right = r12

r1.left = r2
r1.right = r22

r12.right = r23

r2.left = r3
r2.right = r32

r22.right = r33

s = Solution()
print(s.pathSum(r0, 8))

a11 = TreeNode(5)
a21 = TreeNode(4)
a22 = TreeNode(8)
a31 = TreeNode(11)
a32 = TreeNode(13)
a33 = TreeNode(4)
a41 = TreeNode(7)
a42 = TreeNode(2)
a43 = TreeNode(5)
a44 = TreeNode(1)

a11.left = a21
a11.right = a22

a21.left = a31
a22.left = a32
a22.right = a33

a31.left = a41
a31.right = a42
a33.left = a43
a33.right = a44

# print(s.pathSum(a11, 22))

b11 = TreeNode(0)
b21 = TreeNode(1)
b22 = TreeNode(1)

b11.left = b21
b11.right = b22

# print(s.pathSum(b11, 1))


c11 = TreeNode(1)
c21 = TreeNode(-2)
c22 = TreeNode(-3)
c31 = TreeNode(1)
c32 = TreeNode(3)
c33 = TreeNode(-2)
c41 = TreeNode(-1)

c11.left = c21
c11.right = c22
c21.left = c31
c21.right = c32
c22.left = c33

c31.left = c41

# print(s.pathSum(c11, 0))

# print(s.pathSum(c11, -2))
# print(s.pathSum(c11, -1))