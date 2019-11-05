# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        res = ListNode(None)
        res.next = head
        l1 = l2 = l3 = res
        while True:
            if l1.next is None:
                break
            l2 = l1.next
            if l2.next is None:
                break
            l3 = l2.next

            l2.next = l3.next
            l3.next = l2
            l1.next = l3
            l1 = l3 = l2
        return res.next