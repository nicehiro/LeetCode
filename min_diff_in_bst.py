# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        res = []

        def inorder(root):
            if root.left:
                inorder(root.left)
            res.append(root.val)
            if root.right:
                inorder(root.right)

        inorder(root)

        s = float("inf")
        for i in range(1, len(res)):
            s = min(s, res[i] - res[i - 1])

        return s
