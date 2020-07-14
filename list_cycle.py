# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        return self.hard(head)

    def easy(self, head):
        d = {}
        while head:
            if head in d:
                return True
            d[head] = True
            head = head.next
        return False

    def hard(self, head):
        if not head or not head.next:
            return False
        i, j = head.next.next, head.next
        while i:
            if i == j:
                return True
            j = j.next
            i = i.next
            if not i:
                return False
            i = i.next
        return False


if __name__ == '__main__':
    solu = Solution()
    node1 = ListNode(3)
    node2 = ListNode(2)
    node3 = ListNode(0)
    node4 = ListNode(-4)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node2
    print(solu.hasCycle(node1))
