
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

class Solution(object):
    def intersect(self, quadTree1, quadTree2):
        """
        :type quadTree1: Node
        :type quadTree2: Node
        :rtype: Node
        """
        if (quadTree1.isLeaf and quadTree1.val) or (quadTree2.isLeaf and not quadTree2.val):
            return quadTree1
        elif (quadTree2.isLeaf and quadTree2.val) or (quadTree1.isLeaf and not quadTree1.val):
            return quadTree2
        else:
            t1 = self.intersect(quadTree1.topLeft,quadTree2.topLeft)
            t2 = self.intersect(quadTree1.topRight,quadTree2.topRight)
            t3 = self.intersect(quadTree1.bottomLeft,quadTree2.bottomLeft)
            t4 = self.intersect(quadTree1.bottomRight,quadTree2.bottomRight)
            if t1.isLeaf and t2.isLeaf and t3.isLeaf and t4.isLeaf and t1.val == t2.val == t3.val == t4.val:
                return t1
            return Node(None,False,t1,t2,t3,t4)
    

