# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        s = [root]
        while s:
            t = s.pop()
            if not t:
                continue
            if t.val == val:
                return t
            else:
                s.append(t.left)
                s.append(t.right)
        return None
