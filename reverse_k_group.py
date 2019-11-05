# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if k == 1:
            return head
        res = ListNode(None)
        res = head
        pointers = []
        for i in range(k+1):
            p = res
            pointers.append(p)
        over = False
        while True:
            for i in range(1, k+1):
                if pointers[i-1].next is None:
                    over = True
                    break
                pointers[i] = pointers[i-1].next
            if over:
                break
            pointers[0].next = pointers[k].next
            pointers[1].next = pointers[k]
            for i in range(k, 1, -1):
                pointers[i].next = pointers[i-1]
        return res.next