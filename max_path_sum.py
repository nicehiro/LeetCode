# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def maxPathSum(self, root: TreeNode) -> int:
        self.max_sum = float('-inf')
        self.recursive(root)
        return self.max_sum

    def recursive(self, root):
        if not root:
            return 0
        left_gain = max(self.recursive(root.left), 0)
        right_gain = max(self.recursive(root.right), 0)
        gain = left_gain + right_gain + root.val
        self.max_sum = max(self.max_sum, gain)
        return root.val + max(left_gain, right_gain)
