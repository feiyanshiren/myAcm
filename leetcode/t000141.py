# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        m = []
        while head:
            if head.next in m:
                return True
            m.append(head)
            head = head.next
        return False

a1 = ListNode(3)
a2 = ListNode(2)
a3 = ListNode(0)
a4 = ListNode(-4)
a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a2
s = Solution()
print(s.hasCycle(a1))
