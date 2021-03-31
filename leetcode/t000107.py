# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        a = []
        if not root:
            return []
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            # node = myQueue.pop(0)
            # print(node.val)
            ll = len(myQueue)
            # a.append(node.val)
            b = []
            for i in range(ll):
                node = myQueue.pop(0)
                b.append(node)
                if node.left:
                    myQueue.append(node.left)
                if node.right:
                    myQueue.append(node.right)
            a.append(b)
        return b[::-1]



def level_queue(root):
        """利用队列实现树的层次遍历"""
        a = []
        if not root:
            return []
        myQueue = []
        node = root
        myQueue.append(node)
        while myQueue:
            # node = myQueue.pop(0)
            # print(node.val)
            ll = len(myQueue)
            # a.append(node.val)
            b = []
            for i in range(ll):
                node = myQueue.pop(0)
                b.append(node.val)
                if node.left:
                    myQueue.append(node.left)
                if node.right:
                    myQueue.append(node.right)
            a.append(b)
        return a[::-1]


r0 = TreeNode(3)
r10 = TreeNode(9)
r11 = TreeNode(20)
r20 = None
r21 = None
r22 = TreeNode(15)
r23 = TreeNode(7)

r0.left = r10
r0.right = r11

r10.left = r20
r10.right = r21
r11.left = r22
r11.right = r23


print(level_queue(r0))
