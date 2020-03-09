# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if head is None or head.val is None:
            return head
        n = 1
        t = p = head
        while t.next is not None:
            n += 1
            t = t.next
        t.next = head
        a = k % n
        i = 0
        while i < (n-a-1):
            p = p.next
            i += 1
        q = p.next
        p.next = None
        return q


def construct(nums_list):
    head = ListNode(None)
    p = head
    for num in nums_list:
        node = ListNode(num)
        p.next = node
        p = p.next
    return head.next

def print_node(head:ListNode):
    while head is not None:
        print(head.val)
        head = head.next

if __name__ == '__main__':
    s = Solution()
    nodes = construct([1,2,3,4,5])
    print_node(s.rotateRight(nodes, 1))
