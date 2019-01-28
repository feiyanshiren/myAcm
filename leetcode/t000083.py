# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        a = ListNode(head.val)
        b = a
        while head.next:
            if head.next.val != a.val:
                a.next = ListNode(head.next.val)
                a = a.next
            head = head.next
        return b


l1 = ListNode(1)
l2 = ListNode(1)
l3 = ListNode(2)
l4 = ListNode(3)
l5 = ListNode(3)
l1.next = l2
l2.next = l3
l3.next = l4
l4.next = l5

s = Solution()

d = s.deleteDuplicates(l1)

while d.next:
    print(d.val)
    d = d.next
print(d.val)
