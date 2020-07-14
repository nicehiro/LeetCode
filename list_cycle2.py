# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head: ListNode) -> ListNode:
        return self.hard(head)

    def easy(self, head):
        d = {}
        i = 0
        while head:
            if head in d:
                return 'tail connects to node index {0}'.format(d[head])
            d[head] = i
            i += 1
            head = head.next
        return 'no cycle'

    def hard(self, head):
        if not head or not head.next:
            return None
        i, j = head.next.next, head.next
        is_cycle = False
        while i:
            if i == j:
                is_cycle = True
                break
            j = j.next
            i = i.next
            if not i:
                break
            i = i.next
        if is_cycle:
            i = head
            while i != j:
                i = i.next
                j = j.next
            return i
        return None


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
    print(solu.detectCycle(node1))
