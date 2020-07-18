# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        first = ListNode(-1)
        first.next = head
        p = first
        while p.next:
            q = first
            f = False
            while q.next != p.next:
                if q.next.val > p.next.val:
                    t = p.next
                    p.next = t.next
                    t.next = q.next
                    q.next = t
                    f = True
                    break
                q = q.next
            if not f:
                p = p.next
        return first.next
