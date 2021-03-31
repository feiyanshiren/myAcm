# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if l1 is None:
            return l2
        if l2 is None:
            return l1
        a = []
        x = l1.val
        y = l1.next
        a.append(x)
        while y is not None:
            x = y.val
            a.append(x)
            y = y.next
        x = l2.val
        y = l2.next
        a.append(x)
        while y is not None:
            x = y.val
            a.append(x)
            y = y.next
        a.sort()
        i = a.pop(0)
        r = ListNode(i)
        k = r
        while len(a):
            i = a.pop(0)
            r1 = ListNode(i)
            r.next = r1
            r = r.next
        return k


k1 = ListNode(1)

k2 = ListNode(2)
k1.next = k2

k3 = ListNode(4)
k2.next = k3
k4 = ListNode(1)

k5 = ListNode(3)
k4.next = k5

k6 = ListNode(4)
k5.next = k6

s = Solution()
d = s.mergeTwoLists(k1, k4)

while d.next is not None:
    print(d.val)
    d = d.next
print(d.val)
    
        