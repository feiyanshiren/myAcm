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
        评论区一个很巧妙的方法，使两个链表到达相等位置时走过的是相同的距离
        链表1的长度是x1+y，链表2的长度是x2+y，我们同时遍历链表1和链表2，到达末尾时，再指向另一个链表。
        则当两链表走到相等的位置时：x1+y+x2 = x2+y+x1
        """
        p = headA
        q = headB
        while p!=q:
            p = p.next if p else headB
            q = q.next if q else headA
        return p 


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
