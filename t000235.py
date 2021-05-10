# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        
class TreeNode2:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.root = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        c = [root]
        a = []
        while len(c) != 0:
            d = c.pop(0)
            a.append(d.val)
            if d.left:
                c.append(d.left)
            if d.right:
                c.append(d.right)
        root2 = TreeNode2(a.pop(0))
        c = [root2]
        while len(c) != 0:
            d = c.pop(0)
            if len(a) != 0:
                d.left = TreeNode2(a.pop(0))
                d.left.root = d
                c.append(d.left)
            if len(a) != 0:
                d.right = TreeNode2(a.pop(0))
                d.right.root = d
                c.append(d.right)
        c = [root2]
        p1 = None
        while len(c) != 0:
            d = c.pop(0)
            if d.val == p.val:
                p1 = d
                break
            if d.left:
                c.append(d.left)
            if d.right:
                c.append(d.right)
        q1 = None
        c = [root2]
        while len(c) != 0:
            d = c.pop(0)
            if d.val == q.val:
                q1 = d
                break
            if d.left:
                c.append(d.left)
            if d.right:
                c.append(d.right)
        a1 = []
        b1 = []
        while p1:
            a1.append({p1.val: p1})
            if p1.root:
                p1 = p1.root
            else:
                p1 = None
        while q1:
            b1.append({q1.val: q1})
            if q1.root:
                q1 = q1.root
            else:
                q1 = None
        # print(a1)
        # print(b1)
        for i in a1:
            for j in b1:
                ii = list(i.keys())[0]
                jj = list(j.keys())[0]
                if ii == jj:
                    # print(ii)
                    k = list(i.values())[0]
                    print(k.val)
                    return k
                
        
    

a = [5, 3, 6, 2, 4, None, None, 1]

root = TreeNode(a.pop(0))

c = [root]

while len(c) != 0:
    d = c.pop(0)
    if len(a) != 0:
        d.left = TreeNode(a.pop(0))
        c.append(d.left)
    if len(a) != 0:
        d.right = TreeNode(a.pop(0))
        c.append(d.right)


"""
def ii(a, r):
    if r is None:
        return None
    if len(a) == 0:
        return r
    elif len(a) == 1:
        r.left = TreeNode(a.pop(0))
    elif len(a) == 2:
        r.left = TreeNode(a.pop(0))
        r.right = TreeNode(a.pop(0))
    else:
        r.left = TreeNode(a.pop(0))
        r.right = TreeNode(a.pop(0))
        ii(a, r.left)
        ii(a, r.right)
    return r

root = ii(a, TreeNode(a.pop(0)))
"""
"""
c = [root]

while len(c) != 0:
    d = c.pop(0)
    print(d.val)
    if d.left:
        c.append(d.left)
    if d.right:
        c.append(d.right)
"""

# print(root)

s = Solution()
print(s.lowestCommonAncestor(root, TreeNode(6), TreeNode(1)))
# print(s.lowestCommonAncestor(root, TreeNode(2), TreeNode(4)))
        