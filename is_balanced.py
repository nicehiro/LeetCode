# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        return self.recursive(root)[1]

    def recursive(self, root):
        if not root:
            return 0, True
        l_left, is_left_balanced = self.recursive(root.left)
        l_right, is_right_balanced = self.recursive(root.right)
        if is_left_balanced and is_right_balanced and abs(l_left - l_right) <= 1:
            return max(l_left, l_right) + 1, True
        return max(l_left, l_right) + 1, False
