# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def sortedListToBST(self, head: ListNode) -> TreeNode:
        if not head:
            return None
        self.head = head
        l = self.calc_len()
        return self.recursive(0, l)

    def calc_len(self):
        l = 1
        p = head
        while p.next:
            l += 1
            p = p.next
        return l

    def recursive(self, s, e):
        if s >= e:
            return None
        m = (s + e) // 2
        left = self.recursive(s, m)
        root = TreeNode(self.head.val)
        self.head = self.head.next
        right = self.recursive(m+1, e)
        root.left = left
        root.right = right
        return root
