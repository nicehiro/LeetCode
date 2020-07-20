# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def sortList(self, head: ListNode) -> ListNode:
        return self.recursive(head)

    def recursive(self, head: ListNode):
        if not head:
            return None
        if not head.next:
            return head
        mid = self.find_mid(head)
        left = head
        right = mid.next
        mid.next = None
        left = self.recursive(left)
        right = self.recursive(right)
        return self.combine(left, right)

    def find_mid(self, head: ListNode):
        fast = slow = ListNode(-1)
        fast.next = head
        while fast.next:
            fast = fast.next
            slow = slow.next
            if not fast.next:
                break
            fast = fast.next
        return slow

    def combine(self, left: ListNode, right: ListNode) -> ListNode:
        head = ListNode(-1)
        p = head
        while left and right:
            if left.val <= right.val:
                p.next = left
                left = left.next
            else:
                p.next = right
                right = right.next
            p = p.next
        if left:
            p.next = left
        elif right:
            p.next = right
        return head.next

def print_list(head: ListNode):
    while head:
        print(head.val, end='\t')
        head = head.next
    print()


if __name__ == '__main__':
    solu = Solution()
    node1 = ListNode(-1)
    node2 = ListNode(5)
    node3 = ListNode(3)
    node4 = ListNode(4)
    node5 = ListNode(0)
    node1.next = node2
    node2.next = node3
    node3.next = node4
    node4.next = node5
    print_list(node1)
    res = solu.sortList(None)
    print_list(res)
