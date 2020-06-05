# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        return self.recursive(root.left, root.right)

    def recursive(self, l: TreeNode, r: TreeNode):
        if not l and not r:
            return True
        if not l or not r:
            return False
        if l.val != r.val:
            return False
        return self.recursive(l.left, r.right) and self.recursive(l.right, r.left)

    def iteration(self):
        pass
