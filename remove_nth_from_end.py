# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        l = 1
        p = head
        while p.next is not None:
            l += 1
            p = p.next
        p = head
        if l-n-1 < 0:
            return head.next
        for i in range(l-n-1):
            p = p.next
        e = p.next.next
        p.next = e
        return head


if __name__ == '__main__':
    s = Solution()
    l1 = ListNode(1)
    l2 = ListNode(2)
    l3 = ListNode(3)
    l4 = ListNode(4)
    l5 = ListNode(5)
    l1.next
    s.removeNthFromEnd()
            
