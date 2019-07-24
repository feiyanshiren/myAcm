# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if not head or not head.next:
            return True
        slow = head
        fast = head
        while fast:
            slow = slow.next
            fast = fast.next.next if fast.next else fast.next
        slow = self.rev(slow)
        while head and slow:
            if head.val != slow.val:
                return False
            else:
                head = head.next
                slow = slow.next
        return True
        
    """
     while q:
        res,q.next,q = q,res,q.next
    """
    def rev(self, h: ListNode):
        if not h or not h.next:
            return h
        p = self.rev(h.next)
        h.next.next = h
        h.next = None
        return p


a = [1, 2 ]
b = [ListNode(a[0])]
for i in range(1, len(a)):
    b.append(ListNode(a[i]))
    b[i - 1].next = b[i]

   
s = Solution()
print(s.isPalindrome(b[0])) 