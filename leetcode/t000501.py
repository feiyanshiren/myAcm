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
        def fm(r):
            if not r:
                return
            else:
                m[r.val] = m.get(r.val, 0) + 1
                fm(r.left)
                fm(r.right)
        fm(root)
        a = sorted(m.items(), key=lambda x: x[1], reverse=True)
        res = []
        if len(a):
            mx = a[0][1]
            for i in a:
                if i[1] == mx:
                    res.append(i[0])
                else:
                    break
        return res

t = TreeNode(1)
t12 = TreeNode(2)
t22 = TreeNode(2)
t.right = t12
t12.right = t22
s = Solution()
print(s.findMode(t))
