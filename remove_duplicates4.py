# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None:
            return None
        l = r = head
        while r.next is not None:
            r = r.next
            if l.val == r.val:
                l.next = r.next
            else:
                l = l.next
        return head


def print_node(n: ListNode):
    while n is not None:
        print(n.val, end='\t')
        n = n.next
    print('')


def construct(l: list):
    if l is None or len(l) == 0:
        print(None)
    t = head = ListNode(None)
    for i in l:
        n = ListNode(i)
        t.next = n
        t = t.next
    return head.next


if __name__ == '__main__':
    solu = Solution()
    head = construct([1,1,2,3,3])
    print_node(head)
    head = solu.deleteDuplicates(head)
    print_node(head)
