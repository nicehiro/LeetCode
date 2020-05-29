# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        if root is None:
            return True
        m = 2 ** 10
        return self.recursive(root, m, -1)

    def recursive(self, n: TreeNode, high, low):
        l = r = True
        if n.left is not None:
            if low < n.left.val < n.val:
                l = self.recursive(n.left, n.val, low)
            else:
                return False
        if n.right is not None:
            if high > n.right.val > n.val:
                r = self.recursive(n.right, high, n.val)
            else:
                return False
        return l and r
