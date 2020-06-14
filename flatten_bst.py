# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        # self.last = None
        # self.recursive(root)
        a = root
        self.m2(a)

    def recursive(self, root: TreeNode):
        """Best method.
        """
        if not root:
            return
        self.recursive(root.right)
        self.recursive(root.left)
        root.left = None
        root.right = self.last
        self.last = root

    def m2(self, root: TreeNode):
        if not root:
            return
        if root.left:
            t = root.right
            root.right = root.left
            root.left = None
            a = root
            while a.right:
                a = a.right
            a.right = t
        self.m2(root.right)
