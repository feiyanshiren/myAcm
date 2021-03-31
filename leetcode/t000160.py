# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def getIntersectionNode(self, headA, headB):
        """
        :type head1, head1: ListNode
        :rtype: ListNode
        """
        l1 = []
        l2 = []
        while headA:
            l1.append(headA)
            headA = headA.next
        while headB:
            l2.append(headB)
            headB = headB.next
        le = [len(l1), len(l2)]
        r = None
        b = -min(le) - 1
        for i in range(-1, b, -1):
            if l1[i] == l2[i]:
                r = l1[i]
            else:
                break
        return r


a1 = ListNode(4)
a2 = ListNode(1)
a3 = ListNode(8)
a4 = ListNode(4)
a5 = ListNode(5)

b1 = ListNode(5)
b2 = ListNode(0)
b3 = ListNode(1)
# b4 = ListNode(8)
# b5 = ListNode(4)
# b6 = ListNode(5)

a1.next = a2
a2.next = a3
a3.next = a4
a4.next = a5
b1.next = b2
b2.next = b3
b3.next = a3

s = Solution()
print(s.getIntersectionNode(a1, b1))
