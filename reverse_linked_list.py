# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        if m == n:
            return head
        f = ListNode(None)
        f.next = head
        a = i = j = k = f
        t = 0
        flag = False
        finish = False
        while k.next is not None:
            t += 1
            k = k.next
            if t == m-1:
                a = k
            if t == m:
                i = k
                j = k
                flag = True
                k = k.next
                t += 1
            while flag and t <= n:
                l = k.next
                k.next = j
                j = k
                k = l
                finish = True
                t += 1
            if finish:
                break
        a.next = j
        i.next = k
        return f.next


def construct(nodes):
    head = ListNode(None)
    l = head
    for n in nodes:
        node = ListNode(n)
        l.next = node
        l = l.next
    return head.next


def print_nodes(head):
    if head.val is None:
        head = head.next
    while head is not None:
        print(head.val, end='\t')
        head = head.next
    print()


if __name__ == '__main__':
    solu = Solution()
    nodes = [3, 5]
    head = construct(nodes)
    print_nodes(head)
    f = solu.reverseBetween(head, 1, 2)
    print_nodes(f)

