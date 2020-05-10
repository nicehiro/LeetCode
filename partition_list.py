# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = ListNode(None)
        after = ListNode(None)
        b_p, a_p = before, after
        while head is not None:
            if head.val >= x:
                a_p.next = head
                a_p = a_p.next
            else:
                b_p.next = head
                b_p = b_p.next
            t = head.next
            head.next = None
            head = t
        b_p.next = after.next
        return before.next


def construct(nodes: list):
    head = ListNode(None)
    p = head
    for val in nodes:
        node = ListNode(val)
        p.next = node
        p = p.next
    return head.next

def print_node(head: ListNode):
    if head.val is None:
        head = head.next
    while head is not None:
        print('{0}'.format(head.val), end='\t')
        head = head.next
    print()


if __name__ == '__main__':
    solu = Solution()
    nodes = [1,4,3,2,5,2]
    head = construct(nodes)
    print_node(head)
    print_node(solu.partition(head, 3))
