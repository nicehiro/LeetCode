# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution :
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        p_a, p_b = headA, headB
        while p_a and p_b:
            p_a = p_a.next
            p_b = p_b.next
        if not p_a:
            p_a = headB
        if not p_b:
            p_b = headA
        while p_a and p_b:
            p_a = p_a.next
            p_b = p_b.next
        if not p_a:
            p_a = headB
        if not p_b:
            p_b = headA
        while p_a and p_b:
            if p_a == p_b:
                return p_a
            p_a = p_a.next
            p_b = p_b.next
        return None
