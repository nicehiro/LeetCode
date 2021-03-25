# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        pass

    def method1(self, head):
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

    def method2(self, head: ListNode) -> ListNode:
        if not head:
            return head
        stack = []

        while head:
            flag = False
            while stack and stack[-1].val == head.val:
                flag = True
                stack.pop(-1)
                stack.append(head)
                head = head.next
            if flag:
                stack.pop(-1)
            if stack:
                stack[-1].next = head
            stack.append(head)
        return stack[0]

    def method3(self, head):
        if not head or not head.next:
            return head
        dummy = ListNode(0)
        dummy.next = head
        pre = dummy
        curr = head
        while curr:
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            if pre.next == curr:
                pre = pre.next
            else:
                pre.next = curr.next
            curr = curr.next
        return dummy.next


def print_node(n: ListNode):
    while n is not None:
        print(n.val, end="\t")
        n = n.next
    print("")


def construct(l: list):
    if l is None or len(l) == 0:
        print(None)
    t = head = ListNode(None)
    for i in l:
        n = ListNode(i)
        t.next = n
        t = t.next
    return head.next


if __name__ == "__main__":
    solu = Solution()
    head = construct([1, 2, 3, 3, 4, 4, 5])
    print_node(head)
    res = solu.deleteDuplicates(head)
    print_node(res)
