# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        last = res = ListNode(None)
        last.next = head
        first = end = head
        while end.next is not None:
            end = end.next
            if first.val != end.val and first.next is not end:
                last.next = end
                first = end
            elif first.val != end.val and first.next is end:
                last = first
                first = end
            elif end.next is None:
                if first.val == end.val:
                    last.next = None
        return res.next


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
    head = construct([1,2,3,3,4,4,5])
    print_node(head)
    res = solu.deleteDuplicates(head)
    print_node(res)
