# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root:
            return False
        self.sum = sum
        return self.recursive(root, 0)

    def recursive(self, root, sumation):
        sumation += root.val
        if not root.left and not root.right:
            if sumation == self.sum:
                return True
            return False
        if root.left and not root.right:
            return self.recursive(root.left, sumation)
        if root.right and not root.left:
            return self.recursive(root.right, sumation)
        return self.recursive(root.left, sumation) or self.recursive(root.right, sumation)
