# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def minDepth(self, root: TreeNode) -> int:
        if not root:
            return 0
        self.min_dep = float('inf')
        self.recursive(root, 0)
        return self.min_dep

    def recursive(self, root, d):
        if not root.left and not root.right:
            self.min_dep = d if d < self.min_dep else self.min_dep
        if root.left:
            self.recursive(root.left, d+1)
        if root.right:
            self.recursive(root.right, d+1)
