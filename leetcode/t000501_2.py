from typing import List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def findMode(self, root: TreeNode) -> List[int]:
        m = {}
        if not root:
            return []
        s = [root]
        while len(s):
            b = s.pop()
            m[b.val] = m.get(b.val, 0) + 1
            if b.left:
                s.append(b.left)
            if b.right:
                s.append(b.right)
        mx = max(m.values())
        res = []
        for k, v in m.items():
            if v == mx:
                res.append(k)
        return res

t = TreeNode(1)
t12 = TreeNode(2)
t22 = TreeNode(2)
t.right = t12
t12.right = t22
s = Solution()
print(s.findMode(t))
