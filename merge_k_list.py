from typing import List
from functools import reduce


# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:

    def construct_list_node(self, l):
        l = [ListNode(x) for x in l]
        length = len(l)
        for i in range(length - 1):
            n = l[i]
            n.next = l[i+1]
        return l[0]

    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        l = len(lists)
        if l == 1:
            return lists[0]
        if l > 2:
            A = self.mergeKLists(lists[:l//2])
            B = self.mergeKLists(lists[l//2:])
            temp = [A, B]
            return self.mergeKLists(temp)
        if l == 2:
            return self.merge2Lists(lists[0], lists[1])
        
    def merge2Lists(self, A, B):
        res = h = ListNode(None)
        while A is not None and B is not None:
            if A.val < B.val:
                h.next = A
                A = A.next
            else:
                h.next = B
                B = B.next
            h = h.next
        if A is not None:
            h.next = A
        else:
            h.next = B
        return res.next


if __name__ == '__main__':
    s = Solution()
    l1 = [1, 4, 5]
    l2 = [1, 3, 4]
    l3 = [2, 6]
    l1 = s.construct_list_node(l1)
    l2 = s.construct_list_node(l2)
    l3 = s.construct_list_node(l3)
    l = [l1, l2, l3]
    print(s.mergeKLists(l))