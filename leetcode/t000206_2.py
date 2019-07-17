# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseList(self, head):
        if not head:
            return None
        return self.reverse(head, head, head.next)
    
    def reverse(self, head, first, target):
        if not target:
            return head
        first.next = target.next
        t = None
        if target.next:
            t = ListNode(target.next.val)
            t.next = target.next.next
        target.next = head
        return self.reverse(target, first, t)
    

a = [1, 2, 3, 4, 5]
b = [ListNode(1)]
for i in range(1, len(a)):
    b.append(ListNode(a[i]))
    b[i - 1].next = ListNode(a[i])
    

s = Solution()
print(s.reverseList(b[0]))