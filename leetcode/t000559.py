
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

class Solution:
    def maxDepth(self, root: 'Node') -> int:
        if not root:
            return 0
        elif root.children == []:
            return 1
        else:
            h = []
            for i in root.children:
                h.append(self.maxDepth(i))
            return max(h) + 1
        

