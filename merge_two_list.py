# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        res = temp = ListNode(0)
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                l3 = l1
                l1 = l1.next
            else:
                l3 = l2
                l2 = l2.next
            temp.next = l3
            temp = temp.next
        if l1 is not None:
            temp.next = l1
        else:
            temp.next = l2
        return res.next