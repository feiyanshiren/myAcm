
# Definition for a Node.
class Node(object):
    def __init__(self, val, children):
        self.val = val
        self.children = children


class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root:
            return []
        r = []
        r.append([root])
        f = []
        while len(r):
            s = []
            d = r.pop(0)
            for i in d:
                s.append(i.val)
                if i.children:
                    if len(r):
                        r[0] = r[0] + i.children
                    else:
                        r.append(i.children)
            f.append(s)
        return f
                


b1 = Node(5, None)
b2 = Node(0, None)
children2 = [b1, b2]
children3 = [Node(6, None)]
a1 = Node(10, children2)
a2 = Node(3, children3)
# a3 = Node(4, None)
children1 = [a1, a2, ]  # a3]
root = Node(1, children1)
s = Solution()
print(s.levelOrder(root))
