# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        if not head:
            return None
        p = q = head
        while q.next:
            p = p.next
            q = q.next
            if q.next:
                q = q.next
        # p: last node of first half
        # q: final node
        q = p.next
        p.next = None
        # reverse second half
        while q:
            r = q.next
            q.next = p.next
            p.next = q
            q = r
        q = p.next
        p.next = None
        s = head
        while q:
            r = q.next
            q.next = s.next
            s.next = q
            s = q.next
            q = r
        return p


if __name__ == '__main__':
    solu = Solution()
    node1 = ListNode(1)
    node2 = ListNode(2)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    solu.reorderList(node1)
